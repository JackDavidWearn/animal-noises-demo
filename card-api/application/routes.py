from application import app
from flask import request, jsonify, Response

@app.route('/get-card', methods=['POST'])
def card():
    cards = request.get_json()
    symbol = cards["value"]
    suit = cards["suit"]
    values = {'A':'Ace', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', 'J':'Jack','Q':'Queen','K':'King'}
    value = values[symbol]
    return jsonify({"value": value, "suit": suit})


    # card_data = request.get_json()
    # card_value = card_data["Value"]
    # card_suit = card_data["Suit"]
    # values = {"Ace":"Ace", "Two":"Two", "Three":"Three", "Four":"Four", "Five":"Five", "Six":"Six", "Seven":"Seven", "Eight":"Eight", "Nine":"Nine", "Ten":"Ten", "Jack":"Jack", "Queen":"Queen", "King":"King"}
    # suits = {"Clubs":"Clubs", "Diamonds":"Diamonds", "Hearts":"Hearts", "Spades":"Spades"}
    # selected_card = f"{values[card_value]} of {suits[card_suit]}"
    # return Response(selected_card, mimetype='text/plain')