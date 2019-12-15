import pytest
from flask import g, session
from app.db import get_db


def test_register(client, app):
    assert client.get('/register').status_code == 200
    response = client.post(
        '/register', data={'username': 'a@b.com', 'password': 'a'}
    )
    assert 'http://localhost/login' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from user where username = 'a@b.com'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a@c.com', '', b'Password is required.'),
    # ('a@b.com', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
