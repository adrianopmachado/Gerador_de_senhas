import random

print('Gerador de senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,0123456789'

quantidade = input('Informe em números a quantidade de senhas você deseja gerar? ')
quantidade = int(quantidade)

valores = input('Informe em números a quantidade de caracteres que você deseja nas senhas: ')
valores = int(valores)

print('Suas senhas geradas:')

for senha in range(quantidade):
    senhas = ''
    for caract in range(valores):
        senhas += random.choice(caracteres)
    print(senhas)


