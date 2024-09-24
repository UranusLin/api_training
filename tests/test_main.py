from fastapi.testclient import TestClient
from api.main import app
import pytest

client = TestClient(app)


def test_predict_endpoint():
    response = client.post("/predict/v1", json={
        "business_unit": "C170",
        "request_id": "ca0a1a91-376-41d2-a03a-4ee82445d40",
        "inputs": {
            "cust_no": "176ZpUZczEtk29&9+w1Fgw==",
            "date": "2022-01-07 09:40:50"
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert data["outputs"]["status_code"] == "0000"
    assert data["outputs"]["status_msg"] == "API success"


def test_invalid_cust_no():
    response = client.post("/predict/v1", json={
        "business_unit": "C170",
        "request_id": "ca0a1a91-376-41d2-a03a-4ee82445d40",
        "inputs": {
            "cust_no": "short",
            "date": "2022-01-07 09:40:50"
        }
    })
    assert response.status_code == 400
    assert "cust_no should be 24 characters long" in response.text


def test_invalid_date():
    response = client.post("/predict/v1", json={
        "business_unit": "C170",
        "request_id": "ca0a1a91-376-41d2-a03a-4ee82445d40",
        "inputs": {
            "cust_no": "176ZpUZczEtk29&9+w1Fgw==",
            "date": "invalid-date"
        }
    })
    assert response.status_code == 400
    assert "Invalid date format" in response.text
