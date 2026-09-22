# Solicitando a idade e a altura 
idade = int(input("Coloque sua idade: "))
altura = float(input("Coloque sua altura (M): "))

# Validando os dados 
entrada = (idade >= 12) and (altura >= 1.40) 

print("Entrada aprovada : ", entrada) 

