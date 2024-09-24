'''
Crie um programa que receba do usuário as seguintes informações:
- Nome
- CPF
- Telefone
- E-mail
- Endereço 
- Gênero
- Escolaridade
- Signo 
- Tipo sanguíneo

'''

# entrada de dados
print("Por gentileza, nos informe as seguintes informações")
nome = input("Insira seu nome: ")
cpf = int(input("Insira seu CPF: "))
telefone = int(input("Insira seu número: "))
email = input("Insira o seu email: ")
endereco = input("Insira seu endereço: ")
genero = input("Insira seu gênero: ")
escolaridade = input("Insira sua escolaridade: ")
signo = input("Insira seu signo: ")
sangue = (input("Insira sua tipagem sanguinea: "))

# saida de dados 
print("São essas as suas informações: ")
print(nome)
print(cpf)
print(telefone)
print(email)
print(endereco)
print(genero)
print(escolaridade)
print(signo)
print(sangue)