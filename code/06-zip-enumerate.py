# Criando Listas
lista01 = [1, 2, 3]
lista02 = [1, 4, 8, 6]

# Sempre retorna a união de duas listas com o tamanho da menor em tuplas
print("Iterator em lista da função zip:", list(zip(lista01, lista02)))

# Criando listas
lista03 = ["A", 1, "B"]
lista04 = ["C", "D", 1]

# Sempre retorna a união de duas listas com o tamanho da menor em tuplas
print("Iterator em lista da função zip:", list(zip(lista03, lista04)))

# Criando dicionários
dicionario01 = {"A": 1, "B": 2}
dicionario02 = {"C": 3, "D": 4}

# O relacionamento nesse caso acontece por chaves
print("União dos dicionários por chaves:", list(zip(dicionario01, dicionario02)))

# O relacionamento nesse caso acontece por valores
print("União dos dicionários por valores:", list(zip(dicionario01, dicionario02.values())))

# Criando dicionário vazio
dicionario_trocado = {}

# Chaves de um dicionário recebendo valores de outro, se trocando
for x, y in zip(dicionario01, dicionario02.values()):
    dicionario_trocado[x] = y

# Imprimindo chaves e valores, trocados
print("Chaves:", dicionario_trocado.keys(), "Values:", dicionario_trocado.values())

# Criando listas
lista05 = ['A', 'N', 'T', 'O', 'N', 'I', 'O']

# Imprimindo a enumeração de uma sequência, retorna uma lista de tuplas
print(list(enumerate(lista05)))

# Imprimindo índices e valores
for x, y in enumerate(lista05):
    print("Índice: ", x, "Valor:", y)