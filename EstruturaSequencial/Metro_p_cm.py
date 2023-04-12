# Faça um Programa que converta metros para centímetros.

metro = input("Digite a quantidade de metros: ")

def convertendoMetroEmCm(metro):
# Esta função recebe uma medida em metro e retorta esta medida em centimetros. 
    metro = int(metro) * 100
    return metro

print(f"A quatidade de cm é : {convertendoMetroEmCm(metro)}")