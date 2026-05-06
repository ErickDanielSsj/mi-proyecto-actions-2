from fastapi.testclient import TestClient
from src.main import app

# TestClient simula peticiones HTTP sin levantar el servidor real
client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "API Funcionando"}


def test_obtener_productos():
    response = client.get("/productos")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_obtener_producto_existente():
    response = client.get("/productos/1")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Laptop"


def test_obtener_producto_no_existente():
    response = client.get("/productos/999")
    assert response.status_code == 404


def test_crear_producto():
    nuevo = {"nombre": "Monitor", "precio": 299.99}
    response = client.post("/productos", json=nuevo)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Monitor"
