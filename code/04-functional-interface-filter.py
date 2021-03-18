# Importando a função reduce de functools
from functools import reduce

# Criando uma lista
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando somente os números pares
print("Filtering:", list(filter(lambda n: n % 2 == 0, lista)))

# Reduzindo até o maior valor mas antes realizando a filtragem
print("Filtering and Reducing:", reduce(lambda x, y: x if(x > y) else y, list(filter(lambda n: n % 2 == 0, lista))))