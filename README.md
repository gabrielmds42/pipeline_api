# ETL Pipeline com Python, Requests, PostgreSQL e Streamlit

Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) utilizando Python e a biblioteca `requests` para obtenção de dados via API. O banco de dados utilizado é o PostgreSQL, rodando em um contêiner Docker, e os dados podem ser visualizados via Streamlit, também rodando em Docker.

## 📌 Objetivo
Criar um pipeline de ETL simples e modular que:
1. **Extrai** dados de uma API utilizando `requests`.
2. **Transforma** os dados para um formato estruturado.
3. **Carrega** os dados em um banco de dados PostgreSQL.
4. **Visualiza** os dados através de uma aplicação Streamlit.

## 📂 Estrutura do Projeto
```
pipeline_api/
│-- etl/
│   ├── etl.py  
│   ├── models.py  
│-- app/
│   ├── app.py  
│-- requirements.txt  # Dependências do projeto
│-- .env.example  # Exemplo de configuração de variáveis de ambiente
│-- .env  # Arquivo de variáveis de ambiente (não deve ser versionado)
│-- .gitignore  # Arquivo para ignorar arquivos sensíveis
│-- README.md  # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas
- Python 3.x
- `requests` para extração de dados
- `pandas` para transformação
- `PostgreSQL` rodando em uma VPS
- `Streamlit` para visualização dos dados
- `python-dotenv` para gerenciamento de variáveis de ambiente

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone git@github.com:gabrielmds42/pipeline_api.git
   cd pipeline_api
   ```
2. Configure as variáveis de ambiente:
   - Copie o arquivo de exemplo:
     ```bash
     cp .env.example .env
     ```
   - Edite o `.env` e ajuste as configurações do PostgreSQL e da API.
3. Acesse o Streamlit para visualização:
   ```bash
   http://localhost:8501
   ```

## ⚙️ Configuração
Todas as configurações sensíveis, como credenciais e URLs de API, devem ser definidas no arquivo `.env`. Nunca compartilhe este arquivo publicamente. O `.gitignore` já está configurado para evitar a versão do `.env`.

## 📌 Próximos Passos
- Melhorar a gestão de erros na extração
- Adicionar logs para monitoramento do pipeline
- Implementar autenticação na API e na interface Streamlit

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

