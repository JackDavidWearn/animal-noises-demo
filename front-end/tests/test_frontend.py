from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase

class TestBase(TestCase):

    # Creating the application with an sqlite Database
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db', DEBUG = True
        )
        return app
    
    # Setting up the database and plugging in mock data
    def setUp(self):
        sample_result = Results(animal='cat', noise='meow')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()

    # Tearing down the database
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Testing for each of the different animal and animal noises
class TestView(TestBase):

    # Testing for the dog get and post request
    def test_get_frontend_dog(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"dog"})
            m.post('http://noise-api:5000/noise', json={"noise":"woof"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the sample_result is in the database
            self.assertIn(b'dog goes woof', response.data) # Tests to see that the get and post request is in the front-end
            self.assertNotIn(b'cow goes moo', response.data) # Tests to see that the string is not being sent in

    # Testing for the cat get and post request
    def test_get_frontend_cat(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"cat"})
            m.post('http://noise-api:5000/noise', json={"noise":"meow"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the sample_result is in the database
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the get and post request is in the front-end
            self.assertNotIn(b'cow goes moo', response.data) # Tests to see that the string is not being sent in

    # Testing for the cow get and post request
    def test_get_frontend_cow(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"cow"})
            m.post('http://noise-api:5000/noise', json={"noise":"moo"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the sample_result is in the database
            self.assertIn(b'cow goes moo', response.data) # Tests to see that the get and post request is in the front-end
            self.assertNotIn(b'sheep goes baa', response.data) # Tests to see that the string is not being sent in

    # Testing for the sheep get and post request
    def test_get_frontend_sheep(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"sheep"})
            m.post('http://noise-api:5000/noise', json={"noise":"baa"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the sample_result is in the database
            self.assertIn(b'sheep goes baa', response.data) # Tests to see that the get and post request is in the front-end
            self.assertNotIn(b'cow goes moo', response.data) # Tests to see that the string is not being sent in

    # Testing for the pig get and post request
    def test_get_frontend_pig(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"pig"})
            m.post('http://noise-api:5000/noise', json={"noise":"oink"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) # Tests to see that the sample_result is in the database
            self.assertIn(b'pig goes oink', response.data) # Tests to see that the get and post request is in the front-end
            self.assertNotIn(b'cow goes moo', response.data) # Tests to see that the string is not being sent in


