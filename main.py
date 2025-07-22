# Projeto 1: Calculadora de IMC (Índice de Massa Corporal)

print("--- Calculadora de IMC ---")

# Pede o peso e a altura ao usuário e converte para float
# float() é usado para permitir números com casas decimais, como 70.5
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# A fórmula do IMC é: peso / (altura elevada ao quadrado)
imc = peso / (altura ** 2)

# Mostra o resultado para o usuário, formatado com 2 casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Fornece uma interpretação simples do resultado usando if/elif/else
if imc < 18.5:
    print("Classificação: Magreza")
elif imc < 24.9:
    print("Classificação: Normal")
elif imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

print(f"\nAnálise feita em: 22/07/2025")