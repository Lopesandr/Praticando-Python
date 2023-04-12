# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = input("Digite o valor de um lado do quadrado: ")

def calculandoQuadrado(lado):
# Esta função recebe o valor de um lado de um quadrado e retorna a área do quadrado
    return int(lado) ** 2
    

print(f"A área do quadrado em dobra é: {calculandoQuadrado(lado) * 2}")
