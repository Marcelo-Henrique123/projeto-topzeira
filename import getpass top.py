import os
import random
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_console()


nome = input("Digite seu nome: ")
senha = input("Digite a sua senha: ")
nome_funcionario = input("Digite o nome do funcionário: ")

desempenho_prova = int(input("Qual o desempenho dele na prova de admissão?: "))

if desempenho_prova <700:
    print("desempenho insuficiente para admissão")
    exit()

avaliação = input("Qual a avaliação dele nas outras empresas: ")

if avaliação == 'ruim':
    print("Não podemos ter um mal funcionário")
    exit()

cargo = input("qual cargo ele ocupará?: ")

horario = input("Qual o horário de entrada: ")
horario_saida = input("Qual o horario de saída: ")

beneficios = input("Aplicar benefícios?: ")

if beneficios == 'sim':
    beneficios_especificos = input("Quais Benefícios?: ")

else:
     beneficios_especificos = 'nenhum: '

ferias = input("Quantidade de tempo do funcionário nas férias?: ")

cobra_imposto = 0.85
salario = float(input("Digite o valor do salário bruto: "))
salario_liquido = salario * cobra_imposto

promoção = input("Tempo médio de promoção: ")

codigo_de_funcionario = input("gerar código de funcionário?: ")
codigo_aleatorio = random.randint (1000,99999) if codigo_de_funcionario.lower() == 'sim' else"" 

ficha_criminal = input("Antecedentes Criminais:")


clear_console()


print("Seu nome:", nome)
print("senha: ******")
print("Nome do funcionário é:", nome_funcionario)
print("Horário de entrada:", horario)
print("Horário de saída:", horario_saida)
print("Cobrou imposto?:", cobra_imposto)
print("Salário Bruto:", salario)
print("Salário líquido:", salario_liquido)
print("Cargo:", cargo)
print("Teve benefícios?:", beneficios)
print("Férias do funcionário:", ferias)
print("Desempenho no concurso:", desempenho_prova)
print("Tempo médio de promoção", promoção, " anos")
print("código do funcionário:", codigo_aleatorio)
print("Antecedentes Criminais:", ficha_criminal)
print("Avaliação: ", avaliação)