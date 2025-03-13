import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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



def load_dados_pgsql(data):
    pass
    


if __name__ == '__main__':
    while True:
        dados = extract_dados_bitcoin()
        dados_transformados = transform_dados_bitcoin(dados)
        print(dados_transformados)
        time.sleep(5)