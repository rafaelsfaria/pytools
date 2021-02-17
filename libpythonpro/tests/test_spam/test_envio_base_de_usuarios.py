from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='rafael1', email='rafael1@email.com'),
            Usuario(nome='rafael2', email='rafael2@email.com'),
        ],
        [
            Usuario(nome='rafael', email='rafael@email.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rafael@email.com',
        'curso teste',
        'Corpo do email'
    )

    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='rafael', email='rafael@email.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rafaelremetente@email.com',
        'curso teste',
        'Corpo do email'
    )

    enviador.enviar.assert_called_once_with == (
        'rafaelremetente@email.com',
        'rafael@email.com',
        'curso teste',
        'Corpo do email'
    )
