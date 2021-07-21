# ARGUMENTOS POSICIONAIS E ARGUMENTOS NOMEADOS

def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
            .format(nome, sobrenome, idade, sexo))

dados_pessoais("Cláudio", sobrenome="Rogério", idade=30, sexo=True)
# dados_pessoais(idade=30,
#                 sexo=True,
#                 sobrenome="Carvalho",
#                 nome="Cláudio"
#                 )
