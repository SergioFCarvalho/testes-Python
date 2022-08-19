# import calendar
#
# ano = 2022
# mes = 1
# print(calendar.calendar(ano,2))
# nome="Sérgio freire"
# empresa='SSJ'
# qtde_funcionarios=4
# mediaMensalidade=100.0
# print(nome + " trabalha na empresa " + empresa)
# print("Possui: ", qtde_funcionarios, " funcionarios.")
# print("A média da mensalidade é de: " + str(mediaMensalidade))

# nome=input("Digite um funcionário: ")
# empresa=input("Digite a instituição: ")
# qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
# mediaMensalidade=float(input("Digite a média da mensalidade: "))
# print(nome + " trabalha na empresa " + empresa)
# print("Possui: ", qtde_funcionarios, " funcionarios.")
# print("A média da mensalidade é de: " + str(mediaMensalidade))

# nome=input("Digite o nome: ")
# idade=int(input("Digite a idade: "))
# prioridade="NÃO"
# if idade>=65:
#     prioridade="SIM"
# print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? para SIM Digite (S) para Não (N)").upper()
if idade>=65 and doenca_infectocontagiosa=="S":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "S":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "N":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "N":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")