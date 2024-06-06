from unittest import mock


mock_firebase_user = {
    'user_id': 'firebasegenerateduserid',
    'email': 'testuser@gmail.com',
    # ... add more firebase return values
}

# client is from conftest.py
def test_auth(client):
    with mock.patch('auth.auth.verify_id_token') as magic_mock:
        magic_mock.return_value = mock_firebase_user
        post_data = {
            'token': 'firebaserusertokenid'
        }

        response = client.post('/api/auth/token', data=post_data)
        assert response.status_code == 200