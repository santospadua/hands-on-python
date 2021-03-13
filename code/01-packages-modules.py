# Importando módulo math
import math

# Visualizando métodos disponíveis no módulo math
print(dir(math))

# Método que retorna o fatorial de um número
print("Fatorial de 4 =" + str(math.factorial(4)))

# Importando somente o que vai ser utilizado do módulo
from math import sqrt

# Utilizando o método sqrt
print("A raíz quadrade de 9 é:" + str(int(sqrt(9))))

# Retorna a funcionalidade da função
help(sqrt)

# Utilizando uma função de random
from random import choice

# Criando uma lista
lista = [0, 1, 2, 3, 4]

# Imprimindo a 'escolha'
print(choice(lista))

# Importando sample de random
from random import sample

# Gerando uma amostragem aleatória
print("Amostragem:", sample(range(10), 2))

# Importando mean and media from statistics
from statistics import mean, median

# Criando uma segunda lista
lista2 = [2, 4, 6, 5]

# Obtendo média e mediana respectivamente
print("Média e Mediana:", mean(lista2), ", ", median(lista2))

# Importando getcwd do módulo os
from os import getcwd

# Imprimindo o diretório atual
print(getcwd())

# Importando stdout de sys
from sys import stdout

# Imprimindo no console
stdout.write("System console")

# Importando módulo request do package urllib
import urllib.request

# Recebendo o conteúdo de uma requisição
content = urllib.request.urlopen("https://www.gruposervnac.com.br")

# Recebe o conteúdo da página
page = content.read()

# Imprime o objeto de retorno da requisição
print(content)

# Imprime o conteúdo hypertext da página
print(page)

# Utilizando o pacote datetime
import datetime

# Atribuindo a data atual
now = datetime.datetime.now()

# Imprimindo a data e hora atual
print("Hora atual:", now)

# Atribuíndo uma hora específica
time = datetime.time(22, 4, 2)

# Imprimindo a hora
print(time)

# Imprimindo a data
print("Hora:", time.hour, "Segundos:", time.second)

# Retornando hoje
oggi = datetime.date.today()

# Atribuíndo a data de meu nascimento
nasciuto = datetime.date(1997, 3, 3)

# Retornando a data de hoje
print("Data de hoje:", oggi)

# Dias em que vivi até hoje
print("Quantos dias estou vivo:", (oggi - nasciuto).days)