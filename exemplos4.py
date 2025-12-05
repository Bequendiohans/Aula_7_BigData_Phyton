# Dicionário
# Estrutura chave e valor.
# Símbolo {}
# notas = {} # Dicionário vazio
# notas ['Matemática'] = 8.5
# notas ['Português '] = 7.5
# notas ['História'] = 9.5

# print(notas)

# notas ['Matemática'] = 8.0 # Modificar
# notas ['Geografia'] = 10  #Adicionar

# del notas ['História']
# print(notas)

#CADASTRO EM DICIONÁRIO

livros = {}
lista_cadastro = []

for i in range (3):
    titulo = input('Informe o título: ')
    autor = input('Informe o autor: ')
    ano = (input('Informe o ano: '))
    genero = input('Informe o genero: ')

    livro = {
        'Título': titulo,
        'Autor': autor,
        'Ano':ano,
        'Genero':genero
    }

lista_cadastro.append(livros)
print(f'{i+1} livros cadastrados')