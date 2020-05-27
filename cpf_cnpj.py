from validate_docbr import CPF, CNPJ

class Documento:

    # Criando uma Simple Factory Pattern --> através de uma condicional, permite a fábrica decidir
    # o que deve ser instanciado e retornar.
    # Este padrão é considerado uma etapa intermediária entre o Factory Method ou Abstract Factory.
    @staticmethod
    def cria_documento(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return Cpf(doc_str)
        elif len(doc_str) == 14:
            return Cnpj(doc_str)
        else:
            raise ValueError(f'Não existe documento com {len(documento)} digitos!')

class Cpf:
    def __init__(self, cpf):
        if self.cpf_validacao(cpf):
            self.cpf = cpf
        else:
            raise ValueError('Erro: CPF inválido!')

    def __str__(self):
        return self.cpf_formatado()

    def cpf_validacao(self, cpf):
        validador = CPF()
        return validador.validate(cpf) # True --> 11 digitos & válido. False --> inválido

    def cpf_formatado(self):
        # fatia_um = self.cpf[:3]
        # fatia_dois = self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:]
        # return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'
        mascara = CPF()
        return mascara.mask(self.cpf)

class Cnpj:
    def __init__(self, cnpj):
        if self.cnpj_validacao(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError('Erro: CNPJ inválido!')

    def __str__(self):
        return self.cnpj_formatado()

    def cnpj_validacao(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)  # True --> 14 digitos & válido. False --> inválido

    def cnpj_formatado(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)