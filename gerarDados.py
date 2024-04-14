import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from faker import Faker

# Configurar para usar nomes brasileiros
fake = Faker('pt_BR')

# Conectando ao servidor MongoDB
client = MongoClient('localhost', 27017)
db = client['joao_pessoa_db']
locais_collection = db['locaisJP']
eventos_collection = db['eventosJP']

# Lista de categorias e bairros fictícios
categorias = ['Restaurante', 'Café', 'Bar', 'Supermercado', 'Parque', 'Teatro']
bairros = ['Centro', 'Tambaú', 'Manaíra', 'Bessa', 'Cabo Branco', 'Altiplano']

# Gerando locais fictícios
locais = []
for _ in range(200):  # Mínimo de 200 locais
    nome = fake.company()
    categoria = random.choice(categorias)
    bairro = random.choice(bairros)
    longitude = random.uniform(-34.93, -34.76)  # Coordenadas aproximadas de João Pessoa
    latitude = random.uniform(-7.26, -7.08)
    locais.append({
        'nome': nome,
        'categoria': categoria,
        'bairro': bairro,
        'localizacao': {'type': 'Point', 'coordinates': [longitude, latitude]},
        'data': datetime.now() - timedelta(days=random.randint(1, 365)),  # Data aleatória nos últimos 365 dias
        'outra_informacao': f'Informação adicional para {nome}'
    })

# Inserindo locais na coleção de locais
locais_ids = locais_collection.insert_many(locais).inserted_ids

# Gerando eventos fictícios para alguns locais e adicionando referência ao local
eventos = []
for local_id in random.sample(locais_ids, 50):  # Gerando eventos para 50 locais aleatórios
    local = locais_collection.find_one({'_id': local_id})
    eventos.append({
        'nome_evento': f'Evento no {local["nome"]}',
        'local_id': local_id,
        'localizacao': local['localizacao'],
        'data': local['data'] + timedelta(days=random.randint(1, 30)),  # Data aleatória nos próximos 30 dias
        'outra_informacao_evento': f'Informação adicional para evento no {local["nome"]}'
    })

# Inserindo eventos na coleção de eventos
eventos_collection.insert_many(eventos)

print("Dados gerados e inseridos no MongoDB com sucesso!")
