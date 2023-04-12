# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Digite o valor do raio do circulo: "))

def calculandoAreaCirculo(raio):
# Esta função recebe o valor do raio de um circulo e retorna o valor da área de um circulo.
    area =3.14 * (raio ** 2)
    return area

print(f"O valor da area do circulo é: {calculandoAreaCirculo(raio)}")
