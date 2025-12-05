lista_alunos = []
notas_alunos = []

for n in range(5):
    nome = input("Informe o nome do aluno: ")
    notas = int(input(f'Informe a nota de {nome}: '))
    notas_alunos.append(notas)

    print(notas_alunos)

for n in notas_alunos:
    if n >= 6:
        print('Aprovado')
    else:
        print('Reprovados')
