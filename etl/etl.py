import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, BitcoinPreco
import os





load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')


DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)

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
    session = Session()
    try:
        bitcoin_preco = BitcoinPreco(**data)
        session.add(bitcoin_preco)
        session.commit()
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
        session.rollback()
    finally:
        session.close()

    
def pipeline():
    dados_json = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados_json)
    load_dados_pgsql(dados_transformados)

if __name__ == '__main__':
    create_database()
    print('Banco de dados criado com sucesso')
    while True:
        pipeline()
        print('Dados inseridos com sucesso')
        time.sleep(15)