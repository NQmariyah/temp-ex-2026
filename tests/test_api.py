# tests/test_api.py
import pytest
from app import app, devices

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Reset database memori sebelum setiap test
        devices.clear() 
        yield client

def test_add_device_success(client):
    """Test skenario normal: Menambahkan device baru"""
    response = client.post('/api/devices', json={
        "name": "Router-A",
        "ip_address": "192.168.1.1"
    })
    assert response.status_code == 201
    assert len(devices) == 1

def test_add_device_missing_field(client):
    """Test pemahaman validasi: Field tidak lengkap harus return 400"""
    response = client.post('/api/devices', json={
        "name": "Switch-A"
        # ip_address sengaja dihilangkan
    })
    assert response.status_code == 400

def test_add_device_duplicate_ip(client):
    """Test pemahaman logika bisnis: IP duplikat harus ditolak (409)"""
    # Insert data pertama
    client.post('/api/devices', json={"name": "Router-A", "ip_address": "10.0.0.1"})
    
    # Insert data kedua dengan IP yang sama
    response = client.post('/api/devices', json={"name": "Router-B", "ip_address": "10.0.0.1"})
    
    assert response.status_code == 409
    assert len(devices) == 1 # Memastikan data kedua tidak masuk
