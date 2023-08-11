nome = input('\nDigite seu nome: ')
idade = int(input('\nDigite sua idade: '))

if idade >= 18:
    print(f'Ola {nome}, você tem {idade} anos e é maior de idade')
else:
    print(f'Ola {nome}, você tem {idade} anos e é menor de idade')