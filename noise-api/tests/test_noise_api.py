from application import app
from flask_testing import TestCase
from flask import url_for

# Creating the TestBase, which returns the created application
class TestBase(TestCase):
    def create_app(self):
        return app

# Testing all of the different noises
class TestView(TestBase):
    
    # Testing the post request for cow
    def test_get_noise_cow(self):
        response = self.client.post(url_for('noise'), json={"animal":"cow"})
        self.assert200(response)
        self.assertIn(b'moo', response.data)

    # Testing the post request for dog
    def test_get_noise_dog(self):
        response = self.client.post(url_for('noise'), json={"animal":"dog"})
        self.assert200(response)
        self.assertIn(b'woof', response.data)
        
    # Testing the post request for sheep
    def test_get_noise_sheep(self):
        response = self.client.post(url_for('noise'), json={"animal":"sheep"})
        self.assert200(response)
        self.assertIn(b'baa', response.data)

    # Testing the post request for cat
    def test_get_noise_cat(self):
        response = self.client.post(url_for('noise'), json={"animal":"cat"})
        self.assert200(response)
        self.assertIn(b'meow', response.data)

    # Testing the post request for pig
    def test_get_noise_pig(self):
        response = self.client.post(url_for('noise'), json={"animal":"pig"})
        self.assert200(response)
        self.assertIn(b'oink', response.data)

    
