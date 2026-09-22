# Criando função maior numero
def maior_numero(x,y):
    if x > y:
        return x

    else:
        return y

# Solicitando os dois numeros ao usuario
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

# chamando a função que verifica o maior numero 
resultado = maior_numero(numero_1,numero_2)

# apresentando o maior numero ao usuario 
print(f"O maior número digitado foi: {resultado}")



