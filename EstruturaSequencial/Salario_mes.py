""" 
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""
salarioHora = input("Digite quanto você ganha por hora: ")
horasMes = input("Digite quantas horas você trabalha no mês: ")

print(f"Voce ira ganhar este valor: {float(salarioHora) * int(horasMes)}")