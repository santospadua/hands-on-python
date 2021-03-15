# Criando função de soma
def soma(x, y):
    return x + y

# Criando função de subtração
def diminuir(x, y):
    return x - y

# Criando duas listas de números
lista01 = [1, 2, 3, 4]
lista02 = [5, 6, 7, 8]

# Iniciando com a função map, retornando um iterator
print("Imprimindo o iterator:", map(lambda x, y: x + y, lista01, lista02))

# Transformando o iterable em uma lista
lista = list(map(lambda x, y: x + y, lista01, lista02))

# Imprimindo a lista
print("Soma dos números correspondentes de cada lista:", lista)

# Retornando o quadrado de um número, por exemplo
def quadrado(x):
    return x ** 2

# Retornando o iterable
print("Imprimindo o iterator:", map(quadrado, lista01))

# Transformando o iterable em uma lista
lista03 = list(map(quadrado, lista01))

# Imprimindo a lista, quadrado dos seus números
print("Lista após a iteração:", lista03)

# Imprimindo em tempo de execução
for numero in list(map(soma, lista01, lista01)):
    print("Soma do próprio número com ele mesmo, lista01:", numero)

# Imprimindo em tempo de execução
for numero in list(map(soma, lista02, lista02)):
    print("Soma do próprio número com ele mesmo, lista02:", numero)

# Criando uma terceira lista auxiliar
auxiliar = [-10, -20, -30]

# Iterando sobre uma expressão lambda dentro de um map convertido para lista
for numero in list(map(lambda x, y, z: abs(x + y + z), lista01, lista02, auxiliar)):
    print("Imprimindo valor absoluto da expressão:", numero)