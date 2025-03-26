import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
users = []

#Testes
def test_create_users():
    new_user = {
        "nome": "Giovanna",
        "email": "test@teste",
        "idade": 23
    }
    reponse = requests.post(f"{BASE_URL}/users", json= new_user)
    assert reponse.status_code == 200
    response_json = reponse.json()
    assert "id" in response_json
    assert "message" in response_json
    users.append(response_json['id'])

def test_get_users():
    reponse = requests.get(f"{BASE_URL}/users")
    assert reponse.status_code == 200
    response_json = reponse.json()
    assert "nomes" in response_json
    assert "total_user" in response_json

def test_get_user():
    if users:
        users_id = users[0]
        reponse = requests.get(f"{BASE_URL}/users/{users_id}")
        assert reponse.status_code == 200
        reponse_json = reponse.json()
        assert users_id == reponse_json['id']

def test_update_task():
    if users:
        user_id= users[0]
        payload = {
            "nome": "Nome",
            "email": "Email",
            "idade": 50
        }
        response = requests.put(f"{BASE_URL}/users/{user_id}" , json=payload)
        response.status_code == 200
        response_json = response.json()
        print(response_json)
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["nome"] == payload["nome"]
        assert response_json["email"] == payload["email"]

def test_delete_user():
    if users:
        user_id = users[0]
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        response.status_code == 200

        response = requests.get(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == 404