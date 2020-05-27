import requests

class Busca_endereco:

    def __init__(self, cep):
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return self.cep_formatado()

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        return False

    def cep_formatado(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json() # Retorna um Dicionário
        # Cria uma Tupla para retornar os Valores
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
