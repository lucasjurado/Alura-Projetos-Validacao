import re

class Telefones:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Numero inválido')

    def __str__(self):
        return self.formatar()

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        return False

    def formatar(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        regex = re.search(padrao, self.numero)
        numero_formatado = f'+{regex.group(1)}({regex.group(2)}){regex.group(3)}-{regex.group(4)}'
        return numero_formatado