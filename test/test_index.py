import os
import tempfile
import pytest
import server
import json

@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            # server.init_db()
            pass
        yield client

    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])


def test_index(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["message"] == "hello world"
