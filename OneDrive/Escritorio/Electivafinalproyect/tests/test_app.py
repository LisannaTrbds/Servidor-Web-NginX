import json
import pytest
from datetime import datetime

def test_hola_mundo(client):
    """Prueba la ruta principal"""
    response = client.get('/')
    
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == 'Hola Mundo desde Python DevOps!'
    assert data['version'] == '1.0.0'
    assert data['framework'] == 'Flask'
    assert 'timestamp' in data

def test_health_check(client):
    """Prueba la ruta de salud"""
    response = client.get('/health')
    
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'OK'
    assert 'message' in data

def test_info_endpoint(client):
    """Prueba la ruta de información"""
    response = client.get('/info')
    
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'app_name' in data
    assert 'python_version' in data
    assert 'flask_version' in data

def test_nonexistent_route(client):
    """Prueba una ruta que no existe"""
    response = client.get('/ruta-inexistente')
    assert response.status_code == 404