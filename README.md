# Repositório de Scripts para a Disciplina de Banco de Dados do Mestrado do IFPB PPGTI

Este repositório contém scripts utilizados para a disciplina de Banco de Dados do Mestrado em Tecnologia da Informação do IFPB - Programa de Pós-Graduação em Tecnologia da Informação.

- [Arquivos](#arquivos)
  - [Script Python](#script-python)
  - [Dump MongoDB](#dump-mongodb)
- [Pastas e Consultas](#pastas-e-consultas)
  - [Total-de-Locais-por-Bairro](/Total-de-Locais-por-Bairro)
  - [Eventos-em-Agosto-de-2023](/Eventos-em-agosto-de-2023)
  - [Locais-Proximos-a-uma-Coordenada-Especifica](/Locais-proximos-a-uma-coordenada-especifica)
  - [Restaurantes-Dentro-de-um-Raio-de-5-km](/Restaurantes-dentro-de-um-raio-de-5-km)
- [Como Rodar o Código em Python](#como-rodar-o-codigo-em-python)
- [Descrição do Código](#descricao-do-codigo)
  - [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
- [Importando o Dump do MongoDB](#importando-o-dump-do-mongodb)
- [Dicionário de Dados](#dicionario-de-dados)

---
## Arquivos:

### Script Python
- **gerarDados.py:** Script em Python utilizado para gerar dados fictícios de locais e eventos e inseri-los no MongoDB.

### Dump MongoDB
- **joao_pessoa_db.agz:** Arquivo de dump do MongoDB que contém o banco de dados `joao_pessoa_db` com dados de locais e eventos.

## Pastas e Consultas:

Cada pasta contém um script que realiza uma consulta específica no banco de dados MongoDB.

1. **Total-de-Locais-por-Bairro:**
   - Consulta para calcular o total de locais por bairro na coleção `locaisJP`.

2. **Eventos-em-Agosto-de-2023:**
   - Consulta para buscar todos os eventos que ocorreram durante o mês de agosto de 2023 na coleção `eventosJP`.

3. **Locais-Proximos-a-uma-Coordenada-Especifica:**
   - Consulta para encontrar locais próximos a uma coordenada geográfica específica na coleção `locaisJP`.

4. **Restaurantes-Dentro-de-um-Raio-de-5-km:**
   - Consulta para buscar todos os restaurantes dentro de um raio de 5 km de uma coordenada específica na coleção `locaisJP`.

## Como Rodar o Código em Python

1. Instale o Python em sua máquina, se ainda não estiver instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
2. Instale as dependências necessárias usando o pip. Abra o terminal e execute o seguinte comando:

```sh
pip install pymongo faker
```
3. Execute o script `gerador_dados_mongodb.py` para gerar e inserir dados fictícios no MongoDB. Certifique-se de que o MongoDB está em execução localmente.

## Descrição do Código

O código em Python `gerador_dados_mongodb.py` utiliza as bibliotecas `pymongo` e `faker` para gerar dados fictícios de locais e eventos e inseri-los em um banco de dados MongoDB local. Ele simula a criação de locais (como restaurantes, cafés, bares, etc.) e eventos associados a esses locais.

### Bibliotecas Utilizadas:

- **pymongo**: O `pymongo` é uma biblioteca Python que permite interagir com o MongoDB a partir de código Python. Ele fornece uma API simples e intuitiva para realizar operações de consulta, inserção, atualização e exclusão de documentos em coleções do MongoDB.

- **faker**: O `faker` é uma biblioteca Python usada para gerar dados fictícios de maneira rápida e conveniente. Ele fornece uma variedade de classes e métodos para criar dados fictícios realistas em diversas áreas, como nomes, endereços, números de telefone, texto, datas, entre outros.

O script também inclui a criação de um índice `2dsphere` na coleção `locaisJP` para permitir consultas geoespaciais com o MongoDB.

Caso não reconheça utilizar o script abaixo no shell do mongo:
```sh
db.locaisJP.createIndex({ "localizacao": "2dsphere" })
```
**Observação:** Certifique-se de ajustar as configurações de conexão do MongoDB no script de acordo com o seu ambiente.

## Importando o Dump do MongoDB

Se você deseja importar o dump do MongoDB no formato BSON (arquivo `joao_pessoa_db.agz`) para restaurar o banco de dados localmente, siga as instruções abaixo:

1. Faça o download do arquivo `joao_pessoa_db.agz` e extraia-o para obter o arquivo BSON (`joao_pessoa_db.bson`).

2. Abra o terminal e navegue até o diretório onde o arquivo BSON (`joao_pessoa_db.bson`) está localizado.

3. Execute o seguinte comando para importar o dump para o MongoDB:
```sh
mongorestore --db joao_pessoa_db --drop --gzip --archive=joao_pessoa_db.agz
```
- `--db joao_pessoa_db`: Especifica o nome do banco de dados para o qual o dump será restaurado.
- `--drop`: Elimina o banco de dados existente antes de restaurar o dump.
- `--gzip`: Indica que o arquivo de dump está compactado com gzip.
- `--archive=joao_pessoa_db.agz`: Especifica o arquivo de dump que será importado.

4. Após a importação, verifique se o banco de dados `joao_pessoa_db` foi restaurado com sucesso no seu ambiente do MongoDB.

# Dicionário de Dados

## LocaisJP

### Variáveis:
- `_id`: Identificador único do documento (ObjectId).
- `nome`: Nome do local (string).
- `categoria`: Categoria do local (string).
- `bairro`: Bairro onde o local está localizado (string).
- `localizacao`: Coordenadas geográficas do local (objeto Point).
  - `type`: Tipo de dado (string, sempre 'Point').
  - `coordinates`: Coordenadas em formato [longitude, latitude] (array).
- `data`: Data associada ao local (data e hora).
- `outra_informacao`: Informação adicional sobre o local (string).
 
## EventosJP


### Variáveis:
- `_id`: Identificador único do evento (ObjectId).
- `nome_evento`: Nome do evento (string).
- `local_id`: Referência ao local onde o evento ocorre (ObjectId).
- `localizacao`: Coordenadas geográficas do evento (objeto Point).
    - `type`: Tipo de dado (string, sempre 'Point').
    - `coordinates`: Coordenadas em formato [longitude, latitude] (array).
- `data`: Data e hora do evento (data e hora).
- `outra_informacao_evento`: Informação adicional sobre o evento (string).