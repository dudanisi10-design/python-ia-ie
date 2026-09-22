# Solicitando idade e se é estudante 
idade = int(input ("Didite sua idade: "))
estudante = input("Você é estudante s/n: ")

# Validando a meia entrada
meia = (idade >= 60) or estudante == "s"

# Apresentando o resultado ao usúario
print("Tem direito a meia-entrada ", meia)

