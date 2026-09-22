#Criando a função verificar idade

def verificar_idade(idade):
    if idade >= 18: 
        return "Maior de idade"
    else:
        return "Menor de idade"
# Solicitando a idade do usuario 
idade_usuario = int(input("Digite sua idade: "))

resultado = verificar_idade(idade_usuario) 

print(resultado)