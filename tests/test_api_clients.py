from api_requests import request_api_clients
import random


class TestApiClients:

    def test_login(self):
        name = 'jhon'
        email = f'anetta{random.randint(0, 999999)}@email.com'  # folosim random ca de fiecare data cand facem run sa nu
        # ne dea eroare - altfel daca incercam cu un singur email de mai multe ori ne va da eroare deja a doua oara
        response = request_api_clients.login(name, email)
        assert response.status_code == 201, f'actual:{response.status_code}, expected: 201'
        assert "accessToken" in response.json().keys(), f'token was not generated. Response: {response.json()}'


#TestApiClients().test_login()
