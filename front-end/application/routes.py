from application import app
from flask import render_template
from application.models import Cards
import requests

@app.route('/')
def index():
    value = requests.get('http://cardvalue-api:5000/get_values')
    suit = requests.get('http://cardsuit-api:5000/get_suit')
    card = {"value": value.text, "suit": suit.text}
    card_gen = requests.post('http://card-api:5000/get_card', json=card)
    json = card_gen.json()
    value = json["value"]
    return render_template('index.html', value=value, suit=suit.text)

    # card_value = requests.get('http://cardvalue-api:5000/get_values')
    # card_suit = requests.get('http://cardsuit-api:5000/get_suit')
    # selected_card = requests.post('http://card_api:5000/get_card', json=card_value.json(), card_suit.json())
    # db.session.add(Results(card_value=card_value.json()["value"], card_suit=card_suit.json()["suit"]))    
    # db.session.commit()
    # results = Results.query.all()
    # return render_template('index.html', results = results)