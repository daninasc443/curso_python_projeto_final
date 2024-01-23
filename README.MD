# Corretoras Brasileiras em Funcionamento

## Trabalho final


## 🔍Como utilizar esse repositório

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
## 📊 ETL - Projeto Final

A ideia do projeto final consiste em buscar dados de uma API (Extract), processar (Transform) e fazer a carga em um banco de dados (Load). 

Visando garantir que a requisição na API fosse bem sucedida, utilizamos a biblioteca "plyer" para implementar a função "notify", que emite um alerta caso a operação falhe. Direcionando, portanto, para uma correção. 

Optamos pelo Brasil API e utilizamos o dado de corretoras brasileiras. 

Esse dado apresentava as seguintes colunas em sua configuração inicial: 

* cnpj
* type
* nome_social
* nome_comercial
* status
* email
* telefone
* cep
* pais
* uf
* municipio
* bairro
* complemento
* logradouro
* data_patrimonio_liquido
* valor_patrimonio_liquido
* codigo_cvm
* data_inicio_situacao
* data_registro
 
Para facilitar a compreensão, essa tabela original foi dividida em tres outras tabelas, sendo:

* Corretoras: 
    * cnpj
    * type
    * nome_social
    * nome_comercial
    * status

* Patrimônios:
    * cnpj
    * data_patrimonio_liquido
    * valor_patrimonio_liquido
    * codigo_cvm
    * data_inicio_situacao
    * data_registro

* Endereços:
    * cnpj
    * email
    * telefone
    * cep
    * pais
    * uf
    * municipio
    * bairro
    * complemento
    * logradouro
    * data_patrimonio_liquido
    * valor_patrimonio_liquido

Além disso foram feitos os devidos tratamentos com o dado, como filtrar apenas corretoras ativas.

Em seguida foi feita a conexão no sqlite e a criação das tabelas respeitando os requistos acima (PK e FK do CNPJ).

Finalmente, foram feitos alguns testes para validar o banco de dados criado.

## 🛠️ Construído com:
Este código foi escrito com auxílio do conteúdo do material do curso de Python para dados da Coderhouse, ChatGPT3.5 e repositórios do Github.
Coderhouse: https://www.coderhouse.com.br/online/python-br
ChatGPT: https://chat.openai.com/
Google Colab:https://colab.google/
Github: https://github.com/ccrivelin/pythoncoderhouse

## 🖇️ Colaborando:
Caso deseje colaborar, entre em contato com os autores para acesso ao repositório do Github: https://github.com/ccrivelin/pythoncoderhouse

## 📌 Versão:
Nós usamos o controle de versão pelo Github através do comando Commit

## ✒️ Autores:
Carolina Crivelin, Daniella Nascimento, Douglas Farias

Responsáveis pelo desenvolvimento, controle de versão e documentação

## 🎁 Expressões de gratidão
Agradecemos ao nosso tutor Felipe Correia por todo apoio durante as aulas e execução do projeto 📢