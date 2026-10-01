# Criando dicionario composto de cadastro de funcionario

funcionarios = {
    "44356":{
        "nome":"Vitor Davi",
        "telefone":"11912121315",
        "data_nascimento":"10/12/2010",
        "cargo":"Jovem Aprendiz",
        "habilidade":["front-end","java","python"]
    },
    "425668":{
        "nome":"Eduarda Vicentina",
        "telefone":"1132826397",
        "data_nascimento":"20/07/2010",
        "cargo":"Jovem Aprendiz",
        "habilidade":["front-end","java","python"]
    },
    "405680":{
        "nome":"Diego Silva",
        "telefone":"11914848315",
        "data_nascimento":"09/09/2009",
        "cargo":"Jovem Aprendiz",
        "habilidade":["front-end","java","python"]
    },

}

print(funcionarios["425668"]["habilidade"][1])