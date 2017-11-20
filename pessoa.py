class Pessoa(object):
    """Classe Pessoa que armazena os dados do cadastro
        em forma de dicionario."""
    def __init__(self):
        self.lista_dados = []


    def set_pessoa(self, dic):
        self.lista_dados.append(dic)


    def get_pessoa(self):
        return self.lista_dados
