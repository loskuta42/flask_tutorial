from flaskapp import create_app


def test_config():
    assert not create_app().testing
    assert create_app
    
def test_wakeup(client):
    response = client.get('/wakeup')
    assert response.data == b'Wake up, Neo...'

