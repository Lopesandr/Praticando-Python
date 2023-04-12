# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import statistics

nota1  = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
listaNotas = [nota1, nota2, nota3, nota4]
print(f"A média das notas é: {statistics.mean(listaNotas)}")
