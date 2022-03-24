from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

# Creating the TestBase, which returns the created application
class TestBase(TestCase):
    def create_app(self):
        return app

# TestView, inherits from TestBase, and used to test all choice operations
class TestView(TestBase):
    # Testing for cow in random choice
    @patch('application.routes.choice', return_value='cow')
    def test_get_animal_cow(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'cow', response.data)

    # Testing for dog in random choice
    @patch('application.routes.choice', return_value='dog')
    def test_get_animal_dog(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'dog', response.data)

    # Testing for cat in random choice
    @patch('application.routes.choice', return_value='cat')
    def test_get_animal_cat(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'cat', response.data)

    # Testing for sheep in random choice
    @patch('application.routes.choice', return_value='sheep')
    def test_get_animal_sheep(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'sheep', response.data)

    # Testing for pig in random choice
    @patch('application.routes.choice', return_value='pig')
    def test_get_animal_pig(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'pig', response.data)

    # Testing for non-existant choice in random choice
    @patch('application.routes.choice', return_value='Jack')
    def test_get_animal_not_exists(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertNotIn(b'jack', response.data)

    