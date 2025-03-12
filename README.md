# ETL Pipeline com Python e Requests

Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) utilizando Python e a biblioteca `requests` para obtenção de dados via API.

## 📌 Objetivo
Criar um pipeline de ETL simples e modular que:
1. **Extrai** dados de uma API utilizando `requests`.
2. **Transforma** os dados para um formato estruturado.
3. **Carrega** os dados em um banco de dados ou arquivo.

## 📂 Estrutura do Projeto
```
ETL_Pipeline/
│-- etl/
│   ├── extract.py  # Função para extração de dados
│   ├── transform.py  # Função para transformação de dados
│   ├── load.py  # Função para carga dos dados
│   ├── config.py  # Configurações do projeto
│-- main.py  # Script principal para rodar o pipeline
│-- requirements.txt  # Dependências do projeto
│-- README.md  # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas
- Python 3.x
- `requests` para extração de dados
- `pandas` para transformação
- `sqlite3` para armazenamento local (ou outro banco de dados conforme necessidade)

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone git@github.com:gabrielmds42/pipeline_api.git
   cd etl-pipeline
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute o pipeline:
   ```bash
   python main.py
   ```

## ⚙️ Configuração
Edite o arquivo `config.py` para ajustar a URL da API, parâmetros e configurações do banco de dados.

## 📌 Próximos Passos
- Melhorar a gestão de erros na extração
- Adicionar logs para monitoramento do pipeline
- Implementar integração com bancos de dados na nuvem

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

