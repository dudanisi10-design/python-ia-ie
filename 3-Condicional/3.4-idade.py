# Dados do paciente
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


# Classificação do paciente 
if id == 0:
    situacao = "RN"
elif idade <= 3:
    situacao = "bebe"
elif idade <= 10:
    situacao = "crianca"
elif idade <= 14:
    situacao = "adolescente"
elif idade <= 30:
    situacao = "jovens"
elif idade <= 64:
    situacao = "adulto"
elif idade >= 64:
    situacao = "vintage"

    print(f"O paciente {nome} é {idade} é ele(a) está {situacao}")