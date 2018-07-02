import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app_client = app.test_client()

    yield app_client


def test_index_page_is_reachable(client):
    content = client.get('/')

    assert b'Hello Docker Flask!' in content.data
