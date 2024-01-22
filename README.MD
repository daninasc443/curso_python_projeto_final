# Corretoras Brasileiras em Funcionamento

## Trabalho final


## Como utilizar esse repositório

Para criar um ambiente virtual, instalar os requisitos você pode seguir os seguintes passos:

1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório do seu projeto.

3. Crie um ambiente virtual usando o comando `python -m venv projeto_final`.

4. Ative o ambiente virtual usando o comando source `projeto_final/bin/activate` (Linux/Mac) ou `projeto_final\Scripts\activate` (Windows).

5. Instale os requisitos do projeto usando o comando `pip install -r requirements.txt`, onde requirements.txt é o arquivo que contém as dependências do projeto.

Para realizar o proceso de ETL, execute o arquivo `get_data.py`, que irá gerar o arquivo corretoras.db, que contém o banco de dados com as informações das corretoras.

```bash
python get_data.py
```