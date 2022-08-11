from application import create_app

def test_fail():
  flask_app = create_app('flask_test.cfg')

  with flask_app.test_client() as test_client:
    # this will fail
    # response = test_client.get('/failure')

    # this will succeed
    response = test_client.get('/fail')

    assert response.status_code == 200
