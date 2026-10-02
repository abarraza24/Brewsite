from app.brewsite import app #Integration test require the app

def test_client():
    client = app.test_client()
    
    response = client.get("/")
    
    
    assert response.status_code == 500
    assert b"Brewery" in response.data