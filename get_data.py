import requests
import pandas as pd
import sqlite3
from plyer import notification

def baixar_dados(url):
    resposta = requests.get(url, timeout=20)

    if resposta.ok:
        dados = resposta.json()
        return dados
    else:
        notification.notify(
            title='Erro de integração na API',
            message='Não foi possível baixar os dados',
            app_name='ETL Corretoras',
            timeout=10
        )
        return None

# Extração dos dados da API
url_api_corretoras = 'https://brasilapi.com.br/api/cvm/corretoras/v1'
dados_corretoras = baixar_dados(url_api_corretoras)

if not dados_corretoras:
    exit()

df_corretoras_cru = pd.DataFrame(dados_corretoras)

# Tratamento de dados
df_corretoras = df_corretoras_cru[['cnpj', 'nome_social', 'nome_comercial', 'status']]
df_corretoras_ativas = df_corretoras[df_corretoras['status'] != 'CANCELADA']

df_patrimonios = df_corretoras_cru[['cnpj', 'data_patrimonio_liquido', 'valor_patrimonio_liquido', 'codigo_cvm', 'data_inicio_situacao', 'data_registro']]

df_enderecos = df_corretoras_cru[['cnpj', 'email', 'telefone', 'cep', 'pais', 'uf', 'municipio', 'bairro', 'complemento', 'logradouro']]

# Carregamento dos dados no banco de dados
conn = sqlite3.connect('corretoras.db')

# Configuração das chaves primárias 
conn.execute('PRAGMA foreign_keys = ON')

# Criação dos relacionamentos e tabelas
conn.execute('''
    CREATE TABLE IF NOT EXISTS patrimonios (
        cnpj TEXT,
        data_patrimonio_liquido TEXT,
        valor_patrimonio_liquido REAL,
        codigo_cvm TEXT,
        data_inicio_situacao TEXT,
        data_registro TEXT,
        FOREIGN KEY (cnpj) REFERENCES corretoras(cnpj)
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS enderecos (
        cnpj TEXT,
        email TEXT,
        telefone TEXT,
        cep TEXT,
        pais TEXT,
        uf TEXT,
        municipio TEXT,
        bairro TEXT,
        complemento TEXT,
        logradouro TEXT,
        FOREIGN KEY (cnpj) REFERENCES corretoras(cnpj)
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS corretoras (
        cnpj TEXT PRIMARY KEY,
        nome_social TEXT,
        nome_comercial TEXT,
        status TEXT
    )
''')

df_corretoras_ativas.to_sql('corretoras', conn, if_exists='replace', index=False)
df_patrimonios.to_sql('patrimonios', conn, if_exists='replace', index=False)
df_enderecos.to_sql('enderecos', conn, if_exists='replace', index=False)


# Validação dos dados
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM corretoras")
total_corretoras = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM patrimonios")
total_patrimonios = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM enderecos")
total_enderecos = cursor.fetchone()[0]

erros = False

if total_corretoras == len(df_corretoras_ativas):
    print("Tabela 'corretoras' foi carregada corretamente")
else:
    erros = True
    notification.notify(
            title='Erro ao carregar os dados',
            message='Não foi possível baixar os dados',
            app_name='ETL Corretoras',
            timeout=10
        )

if total_patrimonios == len(df_patrimonios):
    print("Tabela 'patrimonios' foi carragada corretamente")
else:
    erros = True
    notification.notify(
            title='Erro de integração na API',
            message='Não foi possível baixar os dados',
            app_name='ETL Corretoras',
            timeout=10
        )

if total_enderecos == len(df_enderecos):
    print("Tabela 'enderecos' foi carregada corretamente")
else:
    erros = True
    notification.notify(
            title='Erro de integração na API',
            message='Não foi possível baixar os dados',
            app_name='ETL Corretoras',
            timeout=10
        )

if not erros:
    notification.notify(
            title='Processo de carregamentos finalizado',
            message='Os dados foram carregados com sucesso',
            app_name='ETL Corretoras',
            timeout=10
        )
else:
    notification.notify(
            title='Processo de carregamentos finalizado',
            message='Não foi possível carregar os dados corretamente',
            app_name='ETL Corretoras',
            timeout=10
        )
