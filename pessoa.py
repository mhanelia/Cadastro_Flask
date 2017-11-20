class Pessoa(object):
    """Classe Pessoa que armazena os dados do cadastro
        em forma de dicionario."""
    def __init__(self):
        self.lista_dados = [] # cria uma lista vazia ao iniciar a classe


    def set_pessoa(self, dic):
        self.lista_dados.append(dic) # recebe por parametro o dict_item gerado e armazena no ultimo indice da Lista


    def get_pessoa(self):
        return self.lista_dados #retorna todas os dados salvos dentro da lista
