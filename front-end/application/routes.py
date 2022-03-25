from application import app
from flask import render_template
from application.models import Cards
import requests

@app.route('/')
def index():
    card_value = requests.get('http://cardvalue-api:5000/get_value')
    card_suit = requests.get('http://cardsuit-api:5000/get_suit')
    selected_card = requests.post('http://card_api:5000/get_card', json=card_value.json(), card_suit.json())
    db.session.add(Results(card_value=card_value.json()["value"], card_suit=card_suit.json()["suit"]))    
    db.session.commit()
    results = Results.query.all()
    return render_template('index.html', results = results)