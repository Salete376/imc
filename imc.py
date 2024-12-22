# imc.py - Cálculo do Índice de Massa Corporal
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return f"IMC: {imc:.2f} - Peso adequado"
    elif 25.0 <= imc <= 29.9:
        return f"IMC: {imc:.2f} - Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return f"IMC: {imc:.2f} - Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return f"IMC: {imc:.2f} - Obesidade Grau II"
    else:
        return f"IMC: {imc:.2f} - Obesidade Grau III"

# Entrada do usuário
try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    print(calcular_imc(peso, altura))
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
