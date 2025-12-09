#ATIVIDADES 1 - DICIONÁRIO DE AMIGOS

# amigos = {}

# amigos['João']=20
# amigos['Maria']=22
# amigos['Carlos']=19

# print(amigos['Maria'])

# amigos['Carlos']=20

# amigos['Ana']=21

# del amigos['João']

# print(amigos)

# #ATIVIDADE 2 - LISTA DE MERCADO

# produtos = {}

# produtos['Arroz'] = 25.90
# produtos['Feijão'] = 8.50
# produtos['Leite'] = 5.80

# print(produtos)

# print(produtos['Arroz'])

# produtos['Leite'] = 4.00

# produtos['Açúcar'] = 6.30

# del produtos['Feijão']

# print(produtos)

# #ATIVIDADE 3 - LISTA DE CANDIDATOS

# candidatos = {}
# lst_candidatos = []

# for c in range(5):
#     nome = input('Informe seu nome completo: ')
#     idade = input('Informe sua idade: ')
#     telefone = input('Informe seu número de telefone: ')
#     email = input ('Informe seu e-mail: ')
#     formacao = input('Informe sua formação academica: ')

#     candidatos = {
#     'Nome' : nome,
#     'Idade' : idade,
#     'Telefone' : telefone,
#     'E-mail' : email,
#     'Formacao' : formacao,
#      }

#     lst_candidatos.append(candidatos)
# print(f'{c+1} candidatos registrados.')
# print(lst_candidatos)


# ATIVIDADE 4 -  SELEÇÃO DE ATLETAS (100 METROS)

# atletas = []

# for a in range(5):
#     nome = input("Informe o nome do atleta: ")
#     tempo = float(input(f'Informe o tempo de {nome}: '))
#     categoria = input(f'Informe a categoria de {nome}: ')

#     if tempo <= 12.0:
#         atleta={
#             "nome": nome,
#             "tempo": tempo,
#             "categoria": categoria,
#         }
#         atletas.append(atleta)
#         print(f'{nome} está CLASSIFICADO com {tempo:.2f} segundos, na categoria {categoria}.')
#     else:
#         print(f'{nome} não se classificou.')
# print(atletas)