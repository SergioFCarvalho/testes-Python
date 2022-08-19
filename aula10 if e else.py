# EX da aula 10 if e else
# nome = str(input('Qual seu nome ? '))
# if nome == 'Sérgio':
#     print('Que lindo nome você tem!')
# print(f'Bom dia, {nome}!')

# EX 2
n1 = float(input('Digite sua primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3)/3
print(f'Sua média foi {media:.1f}')
if media>=7:
    print('Aprovado, Parabéns!!!')
else:
    print('Reprovado!!!')
