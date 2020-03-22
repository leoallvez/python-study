"""
    Recebendo dos usuário.
"""
# Entrada de dados
# print("Qual é o seu nome?: ")
nome = input("Qual é o seu nome?: ")

# Exemplo de print antigo 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print antigo 3.x
# print('Seja bem-indo(a) {0}'.format(nome))
# Exemplo print mais moderno 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual a sua idade? ')
idade = int(input('Qual a sua idade?: '))

# Saída de dados
# Exemplo de print antigo 2.x
# print('%s tem %s anos' % (nome, idade))
# Exemplo de print antigo 3.x
# print('{0} tem {1} anos ?'.format(nome, idade))
print(f'{nome} nasceu em {2020 - idade}')

