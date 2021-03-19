# Importando reduce
from functools import reduce

# Utilizando List Comprehension
nome = [letra for letra in "Antonio"]

# Imprimindo o resultado
print(nome)

# List Comprehension de números pares sob uma sequência de números
pares = [numero for numero in range(0, 12) if numero % 2 == 0]

# Imprimindo o resultado
print(pares)

# Criando uma lista para iterable, depois reduzindo
numero = reduce(lambda x, y: x if x > y else y,  [numero for numero in range(0, 12) if numero % 2 == 0])

# Imprimindo o resultado
print(numero)

# Aninhamento em List Comprehension
pares_dos_quadrado = [x for x in [y ** 2 for y in range(0, 12)] if x % 2 == 0]
impares_dos_quadrado = [x for x in [y ** 2 for y in range(0, 12)] if x % 2 != 0]

# Imprimindo os resultados
print("Pares dos quadrados:", pares_dos_quadrado)
print("Ímpares dos quadrados:", impares_dos_quadrado)