# Pipeline API

Este repositório contém um pipeline de engenharia de dados que extrai, transforma e carrega (ETL) dados do preço do Bitcoin em um banco de dados PostgreSQL. O projeto utiliza Python para processamento de dados e um dashboard interativo criado com Streamlit para visualização.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento.
- **Pandas**: Processamento e manipulação de dados.
- **PostgreSQL**: Armazenamento dos dados transformados.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **Requests**: Biblioteca para fazer requisições HTTP e coletar dados da API.
- **Streamlit**: Criação do dashboard interativo.
- **Docker (Opcional)**: Para facilitar a implantação do ambiente.

## Estrutura do Projeto

```
pipeline_api/
│-- etl/
│   ├── etl.py  # Script principal do pipeline ETL
│   ├── models.py  # Definição dos modelos de dados
│-- app/
│   ├── app.py  # Código do dashboard em Streamlit
│-- requirements.txt  # Dependências do projeto
│-- .env.example  # Exemplo de configuração de variáveis de ambiente
│-- .env  # Arquivo de variáveis de ambiente (não deve ser versionado)
│-- .gitignore  # Arquivo para ignorar arquivos sensíveis
│-- README.md  # Documentação do projeto
```

## Instalação e Uso

1. Clone este repositório:

   ```bash
   git clone https://github.com/gabrielmds42/pipeline_api.git
   cd pipeline_api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   - Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais e configurações.

5. Execute o pipeline ETL para coletar dados do Bitcoin:

   ```bash
   python etl/etl.py
   ```

   O script extrai os dados da API da Coinbase, transforma e carrega no banco de dados PostgreSQL a cada 10 minutos.

6. Inicie o dashboard Streamlit para visualizar os dados:

   ```bash
   streamlit run app/app.py
   ```

   O dashboard permite acompanhar a evolução do preço do Bitcoin, ver estatísticas e monitorar execuções do pipeline.

## Docker (Opcional)

Se preferir rodar o projeto em contêineres Docker:

```bash
docker-compose up --build
```

## Contribuição

Fique à vontade para abrir issues e enviar pull requests!

## Autor

Desenvolvido por **Gabriel Magalhães de Souza**. 

- [LinkedIn](https://www.linkedin.com/in/gabriel-magalh%C3%A3es-de-souza/)
- [GitHub](https://github.com/gabrielmds42)

