notas = []

while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break
    notas.append(nota)

print(notas)