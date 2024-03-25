import requests
import random

#metoda ajutatoare pt order api
def get_token():
    body = {
        "clientName" : "Test",
        "clientEmail" : f"dummy_email{random.randint(0,9999999)}@email.com"
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/",json=body)
    return response.json()['accessToken']


def login(client_name,client_email):
    body = {
        "clientName" : client_name,
        "clientEmail" : client_email
    }
    return requests.post("https://simple-books-api.glitch.me/api-clients/",json=body) # obligatoriu json si pe urma ce
    # nume vrem sa ii dam noi
