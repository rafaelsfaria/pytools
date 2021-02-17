from unittest.mock import Mock

import pytest

from libpythonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resultado_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/32245266?v=4'
    resultado_mock.json.return_value = {
        'id': 32245266,
        'avatar_url': url,
        'login': 'rafaelsfaria'
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resultado_mock
    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('rafaelsfaria')
    assert 'https://avatars.githubusercontent.com/u/32245266?v=4' == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('rafaelsfaria')
    assert 'https://avatars.githubusercontent.com/u/32245266?v=4' == url
