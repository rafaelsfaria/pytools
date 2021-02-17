class EnviadorDeSpam():
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo):
        usuarios = self.sessao.listar()

        for usuario in usuarios:
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto,
                corpo
            )
