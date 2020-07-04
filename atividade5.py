from collections import Counter
from collections import defaultdict

users = [
 {"id": 0, "name": "Hero"},
 {"id": 1, "name": "Dunn"},
 {"id": 2, "name": "Sue"},
 {"id": 3, "name": "Chi"},
 {"id": 4, "name": "Thor"},
 {"id": 5, "name": "Clive"},
 {"id": 6, "name": "Hicks"},
 {"id": 7, "name": "Devin"},
 {"id": 8, "name": "Kate"},
 {"id": 9, "name": "Klein"},
]


#print(users)

friendships = [
 (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

#lista de amigos vazia para cada usuário da rede
for user in users:
    user["friends"] = []

#percorre a lista de tuplas adicionando o usuário i à lista do usuário j e vice-versa

#for friendship in friendships:
#    users[friendship[0]]['friends'].append(users[friendship[1]])
#    users[friendship[1]]['friends'].append(users[friendship[0]])

#tuple unpacking
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

#print(users[0])

def number_of_friends(user):
    return len(user['friends'])

#print(number_of_friends(users[2]))

#[2, 3, 3, 2, 3] quantidade de amizades

#para cada usuario na colecao usuarios, eu quero uma expressão: number_of_friends
lista = [number_of_friends(user) for user in users]
#print(lista)

total_connections = sum(number_of_friends(user) for user in users)
#print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users

#print(avg_connections)

#[(0, 2), (1, 3), (2, 3)]


number_of_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

#print(number_of_friends_by_id)

#sorted - função de mais alta ordem, ou seja, pode receber função como parâmetro e devolver função

lista_ordenada = sorted(number_of_friends_by_id, key = lambda num_friends: num_friends[1], reverse=True )
#print(lista_ordenada)

def friends_of_friends_ids_bad(user):
    return [
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
    ]

#funcão decisora = função que toma uma decisão

# def not_the_same (user, other_user):
#     return user['id'] != other_user['id']


# def not_friend(user, other_user):
#     return all(not_the_same(friend, other_user) for friend in user['friends'])

def friends_of_friends_ids (user):
    return set([
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friend(user, foaf)
    ])

#[True, True, False]
#[True, True, True]

#print(friends_of_friends_ids(users[0]))
# contagem = Counter([1, 2, 2, 3, 5, 5, 6, 7, 1])
# print(contagem)

def friends_of_friends_ids_frequency(user):
    return Counter([
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friend(user, foaf)
    ])

# print(friends_of_friends_ids_frequency(users[2]))

interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

def data_scientists_who_like(target_interest):
    return [
        user_id for user_id, interest in interests if interest == target_interest
    ]

# print(data_scientists_who_like('Java'))

#dicionario = {}
#print(dicionario['chave'])

# def teste():
#     return 'aeiou'

# dicionario = defaultdict(teste)
# print(dicionario['chave'])

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)


interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

#print(user_ids_by_interest)

def users_with_common_interests_with (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ])
#print(users_with_common_interests_with(users[0]))

def most_common_interests_with (user):
    return Counter (
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if (interested_user_id != user["id"])
    )
# print(most_common_interests_with(users[0]))



#-------------------------------------------------------------------------------------
            # Atividade Semana 05
# 1 Adicione o atributo “interessado em” aos usuários. 
# Eles podem indicar se estão interessados
# em pessoas do sexo masculino, feminino, ambos ou nenhum.

for user in users: #adicionando o atributo em todos os usuários
    user['interessado em:'] = ''

#definindo o atributo para cada usuário
users[0]['interessado em:'] = 'Mulheres'
users[1]['interessado em:'] = 'Nenhum'
users[2]['interessado em:'] = 'Mulheres'
users[3]['interessado em:'] = 'Mulheres'
users[4]['interessado em:'] = 'Ambos'
users[5]['interessado em:'] = 'Nenhum'
users[6]['interessado em:'] = 'Ambos'
users[7]['interessado em:'] = 'Ambos'
users[8]['interessado em:'] = 'Mulheres'
users[9]['interessado em:'] = 'Homens'


#2 Escreva uma função que faz sugestões de amizade de acordo com o atributo “interessado em”.
#funcão decisora = função que toma uma decisão

def not_the_same (user, other_user):
    return user['id'] != other_user['id']


def not_friend(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user['friends'])


def same_interest (user, other_user):# se possuir o mesmo interesse, a função retorna True
    return user['interessado em:'] == other_user['interessado em:']

def friends_of_friends_ids_same_gender_interests (user):
    return set([
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf) # se não for a mesma pessoa e
        and not_friend(user, foaf)  # se já não for amigo e
        and same_interest(user, foaf) # se possuirem o mesmo 'interessado em:'
    ])

#3 Escreva uma função que faz sugestões de amizade de acordo com o atributo “interessado em” 
# e de acordo com interesses em comum.

common_interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (2, "numpy"), (2, "statsmodel"), (2, "pandas"), 
 (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"), (3, "HBase"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (5, "Haskell"), (5, "programming languages"), 
 (6, "theory"), (6, "decision trees"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), (7, "machine learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

user_ids_by_interest = defaultdict(list)
for user_id, interest in common_interests:
    user_ids_by_interest[interest].append(user_id)


interests_by_user_id = defaultdict(list)
for user_id, interest in common_interests:
    interests_by_user_id[user_id].append(interest)

def users_with_common_interests (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ])


# função que recebe um usuário e retorna a inteseccão de dois conjuntos:
# o conjunto dos usuários com mesmo atributo 'interessado em:' e
# o conjunto dos usuários que possuem o interesse nas mesmas coisas, 

def users_with_common_interests_at_all(user): 
    return friends_of_friends_ids_same_gender_interests(user).intersection(users_with_common_interests(user))


i=0
while i<10:
    print(users[i]['name'], users_with_common_interests_at_all(users[i])) 
    i = i + 1
