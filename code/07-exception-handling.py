# Handling exception com python
try:
    print(1 + 'a')
except TypeError:
    print("Ops!")

# Abertura de arquivos, por exemplo
try:
    file = open("..files/antonio.txt", 'r')
    file.read()
except IOError:
    print("Arquivo não encontrado ou impossibilitado de leitura")
else:
    print("Tudo Ok!")

# Utilizando finally
try:
    file = open("..files/antonio.txt", 'r')
    file.read()
except IOError:
    print("Arquivo não encontrado ou impossibilitado de leitura")
else:
    print("Tudo Ok!")
finally:
    print("Executado")

# Utilizando except sem tipo de erro
try:
    file = open("..files/antonio.txt", 'r')
    file.read()
except:
    print("Arquivo não encontrado ou impossibilitado de leitura")
else:
    print("Tudo Ok!")
finally:
    print("Executado")

# Capturando erro
try:
    file = open("..files/antonio.txt", 'r')
    file.read()
except IOError as error:
    print("Erro sendo mostrado:", error)
else:
    print("Tudo Ok!")
finally:
    print("Executado")