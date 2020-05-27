from datetime import datetime, timedelta

class Data:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        meses_do_ano =['janeiro', 'fevereiro', 'março', 'abril',
                       'maio', 'junho', 'julho', 'agosto', 'setembro',
                       'outubro', 'novembro', 'dezembro']
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro-1]

    def semana_cadastro(self):
        dias_semana = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira',
                       'quinta-feira', 'sexta-feira', 'sábado']
        dia_semana_cadastro = self.momento_cadastro.weekday()
        return dias_semana[dia_semana_cadastro+1]

    def data_formatada(self):
        formacao = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return formacao

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30, hours=15)) - self.momento_cadastro
        return tempo_cadastro