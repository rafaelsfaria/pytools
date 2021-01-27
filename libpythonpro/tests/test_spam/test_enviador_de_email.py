import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_enviar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['rafaelsanfaria@gmail.com', 'teste@test.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'rafael@email.com',
        'assunto',
        'corpo'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'teste.com.br']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
        remetente,
        'rafael@email.com',
        'assunto',
        'corpo'
        )
        assert remetente in resultado
