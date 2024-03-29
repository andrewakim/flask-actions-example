from application import create_app

def test_unknown():
  flask_app = create_app('flask_test.cfg')

  with flask_app.test_client() as test_client:
    response = test_client.get('/unknown')
    assert response.status_code == 200
    assert b"Looks like you're lost." in response.data
