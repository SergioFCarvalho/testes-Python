# Desafio 01
n1 = int(input('Digite um número :'))
n2 = int(input('Digite outro número :'))
s = n1 + n2
print(f'A soma de {n1} e {n2} é {s}')
# obs .format() pode ser usado agora como acima no colocando um f antes das aspas

# Desafio 02
#a = input('Digite algo:')
#print(a.isnumeric(),a.isalpha(),a.isalnum(),a.isdecimal(),a.isupper(),a.isprintable())

# Desafio 2.1

nn = input('Digite algo:')
print('O tipo primitivo é', type(nn))
print('É número ?', nn.isnumeric())
print('É alfabético?', nn.isalnum())
