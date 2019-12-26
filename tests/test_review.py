import pytest
from flask import g, session
from app.db import get_db

@pytest.mark.parametrize('path', (
    'create',
    'edit/1',
    'delete/1',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/login'

def test_author_required(app, client, auth):
    with app.app_context():
        db = get_db()
        db.execute('UPDATE review SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    assert client.post('edit/1').status_code == 403
    assert client.post('delete/1').status_code == 403
    assert b'href="edit/1"' not in client.get('dashboard').data


def test_create(client, auth, app):
    count_prior = 0
    count_after = 0

    with app.app_context():
        db = get_db()
        count_prior = db.execute('SELECT COUNT(id) FROM review').fetchone()[0]

    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'review-text': 'this is a mean review'})

    with app.app_context():
        db = get_db()
        count_after = db.execute('SELECT COUNT(id) FROM review').fetchone()[0]

    assert count_prior + 1 == count_after

def test_edit(client, auth, app):
    auth.login()
    assert client.get('edit/1').status_code == 200
    client.post('edit/1', data={'review-text': 'this is a nice review'})

    with app.app_context():
        db = get_db()
        review = db.execute('SELECT * FROM review WHERE id = 1').fetchone()
        assert review['content'] == 'this is a nice review'

def test_delete(client, auth, app):
    auth.login()
    response = client.post('delete/1')
    assert response.headers['Location'] == 'http://localhost/dashboard'

    with app.app_context():
        db = get_db()
        review = db.execute('SELECT * FROM review WHERE id = 1').fetchone()
        assert review is None
