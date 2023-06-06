#pip install datetime
#pip install yfinance
#pip install pandas


import datetime as dt
import yfinance as yf
import pandas 

# Definir as ações desejadas
lista_acoes = ['^GSPC','^DJI','^TNX', '^BVSP']

# Definir o intervalo de datas desejado
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Criar um dicionário para armazenar os dados das ações
dados_acoes = {}

# Obter os dados de cada ação individualmente
for acao in lista_acoes:
    ticker = yf.Ticker(acao)
    dados = ticker.history(start=data_inicial, end=data_final)
    dados_acoes[acao] = dados

# Exibir os dados das ações
for acao, dados in dados_acoes.items():
    print(f"Dados de {acao:}:")
    dados = dados.drop(columns= ['Dividends', 'Stock Splits'])
    print (dados)
    #display()