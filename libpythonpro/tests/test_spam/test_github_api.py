from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resultado_mock = Mock()
    resultado_mock.json.return_value = {
        'id': 32245266,
        'avatar_url': 'https://avatars.githubusercontent.com/u/32245266?v=4',
        'login': 'rafaelsfaria'
    }
    github_api.requests.get = Mock(return_value=resultado_mock)
    url = github_api.buscar_avatar('rafaelsfaria')
    assert 'https://avatars.githubusercontent.com/u/32245266?v=4' == url
