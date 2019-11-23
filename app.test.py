import os
import unittest
import tempfile

import app


class BasicTestCase(unittest.TestCase):

    def test_home(self):
        tester = app.app.test_client(self)
        pages = ['/', 'about', 'register', 'login']
        for page in pages:
            response = tester.get(page, content_type='html/text')
            self.assertEqual(response.status_code, 200)

    def test_other(self):
        tester = app.app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        tester = os.path.exists("flaskr.db")
        self.assertTrue(tester)

class FlaskrTestCase(unittest.TestCase):

    # set up a new temp database for per test
    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    # destroy the temp database for per test
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    # test messages
    def test_register_messages(self):
        """Test register messages using helper functions."""
        rv = self.register(
            "cat@123.com",
            ""
        )
        assert b'Password is required' in rv.data
        rv = self.register(
            "",
            "123"
        )
        assert b'Username is required' in rv.data

if __name__ == '__main__':
    unittest.main()
