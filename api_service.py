import requests

def send_payment(amount, token):
    response = requests.post("https://api.stripe.com/v1/charges", data={
        "amount": amount,
        "source": token,
        "currency": "AUD"
    })
    return response.json()
