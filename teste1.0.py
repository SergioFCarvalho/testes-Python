#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print(f'Seu nome em maiúsculo é {nome.upper()}') #– O nome com todas as letras maiúsculas e minúsculas.
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome possue {len(nome)- nome.count(" ")} letras') #– Quantas letras ao todo (sem considerar espaços).
divide = nome.split()
print(f'seu Primeiro nome é {divide[0]} e ele tem {len(divide[0])} letras.') #– Quantas letras tem o primeiro nome.
