import pytest
from app import app

@pytest.fixture
def client():
    """Fixture para crear cliente de prueba de Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def runner():
    """Fixture para runner de comandos CLI"""
    return app.test_cli_runner()