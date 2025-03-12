import requests
import time
from tinydb import TinyDB
from datetime import datetime

def extract_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'

    response = requests.get(url)
    data = response.json()

    return data

def transform_dados_bitcoin(data):
    valor = data['data']['amount']
    moeda = data['data']['currency']
    criptomoeda = data['data']['base']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dados_transformados = {
        'valor': valor,
        'moeda': moeda,
        'criptomoeda': criptomoeda,
        'timestamp': timestamp
    }

    return dados_transformados



def load_dados_tinydb(data, db_name='bitcoin.json'):
    db = TinyDB(db_name)
    db.insert(data)
    print('Dados inseridos com sucesso!')


if __name__ == '__main__':
    while True:
        dados = extract_dados_bitcoin()
        dados_transformados = transform_dados_bitcoin(dados)
        load_dados_tinydb(dados_transformados)
        print(dados_transformados)
        time.sleep(5)