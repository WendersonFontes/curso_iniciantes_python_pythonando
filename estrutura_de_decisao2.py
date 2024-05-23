nota1 = int(input('Digite a nota1: '))
nota2 = int(input('Digite a nota2: '))

media = (nota1 +nota2) / 2

if media > 6:
    print('Aprovado')
elif media < 6 and media >=4:
    print('recuperação')
else:
    print('Reprovado')