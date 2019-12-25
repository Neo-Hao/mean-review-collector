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
    ('cat@cat.com', 'test', b'registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/register',
        data={'username': username, 'password': password}
    )
    print(response.data)
    assert message in response.data


def test_login(client, auth):
    assert client.get('/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/dashboard'

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'cat@cat.com'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a@c.com', '123', b'Incorrect username'),
    ('cat@cat.com', '123', b'Incorrect password'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session
