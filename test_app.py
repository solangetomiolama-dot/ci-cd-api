import pytest
from app import app

@pytest.fixture
def client():
    """Crée un client de test pour l'application"""
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Teste la route principale /"""
    response = client.get('/')
    
    # Vérifie que la réponse est 200 OK
    assert response.status_code == 200
    
    # Vérifie le contenu JSON
    data = response.get_json()
    assert data['message'] == "API CI/CD en ligne"

def test_status_route(client):
    """Teste la route /status"""
    response = client.get('/status')
    
    # Vérifie que la réponse est 200 OK
    assert response.status_code == 200
    
    # Vérifie le contenu JSON
    data = response.get_json()
    assert data['status'] == "OK"

def test_404_route(client):
    """Teste qu'une route inexistante renvoie 404"""
    response = client.get('/inexistante')
    assert response.status_code == 404