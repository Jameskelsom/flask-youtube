

def test_api_is_ok(app):
    with app.test_client() as client:
        response = client.get('/api')
        assert response.status_code == 200
        assert str(response.data)
        assert 'Bruno' in str(response.data)