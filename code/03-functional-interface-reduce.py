# Importando a função reduce
from functools import reduce

# Criando uma lista
lista = [10, 21, 30, 82, 41]

# Criando uma função de soma
def soma(x, y):
    return x + y

# Reduce retorna, puts 184
print("Simple reduce:", reduce(soma, lista))

# Isso aqui é obra de arte, desculpem a todos, estou me divertindo
# Somando até o último elemento, ou desconsiderando todos os elementos ímpares

# Puts 122
print("Work with reduce:", reduce(lambda x, y: x + y if(y % 2) == 0 else x + 0, lista))

# Pegando o maior número dentro da lista, Puts 82
print("Work with reduce:", reduce(lambda x, y: x if(x > y) else y, lista))

# Atribuíndo a função a uma variável
functional = lambda x, y: x if(x > y) else y

# Imprimindo a tipagem
print("Verificando a tipagem:", type(functional))