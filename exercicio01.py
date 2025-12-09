lista_notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5, 4.5, 10.0]

for n in lista_notas:
    if n >= 7.0:
        print("APROVADO")
    if 5 >= n < 7.0:
        print("RECUPERACAO")
    if n < 4.0:
        print("REPROVADO")