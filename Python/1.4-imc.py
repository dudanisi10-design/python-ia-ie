# Solicitando o peso e altura ao usuário 
peso = float(input("Digite se peso (Kg): "))
altura = float(input("Digite sua altura (M) "))

# Realizando o calculo do IMC
imc = peso / altura**2

# Apresentando o resultado do IMC ao usuário 
print("O seu IMC é ", imc)
