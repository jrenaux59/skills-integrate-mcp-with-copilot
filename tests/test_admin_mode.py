from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_requires_teacher_login():
    response = client.post('/activities/Chess%20Club/signup?email=student@example.com')
    assert response.status_code == 403


def test_teacher_can_log_in_and_signup():
    login_response = client.post(
        '/login',
        data={'username': 'teacher', 'password': 'Mergington123!'},
        follow_redirects=False,
    )
    assert login_response.status_code == 200

    signup_response = client.post(
        '/activities/Chess%20Club/signup?email=newstudent@example.com'
    )
    assert signup_response.status_code == 200

    logout_response = client.post('/logout')
    assert logout_response.status_code == 200
