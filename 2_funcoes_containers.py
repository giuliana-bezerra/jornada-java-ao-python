#### Funções ####

def nome_da_funcao (parametro1):
    print(parametro1)
    return parametro1

retorno = nome_da_funcao(1)
print("R1:", retorno)
retorno = nome_da_funcao("Giu")
print("R2:", retorno)

def saudacao():
    print("Olá!")

retorno = saudacao()
print(retorno)

def somar(numero1, numero2):
    return numero1 + numero2

print(somar(1, 2))

#### Funções built-in ####

print(len("string"))
print(str(1))
print(int("1"))
print(float(1))
print(int(20.54))
# exceção
# print(int("20.54"))

#age = input("Idade?")
#print("Você tem", age, "anos")


#### Parâmetros e Escopo ####
def f(x=2):
    return x**x

print(f())
print(f(3))


def somar(x, y = 10):
    return x + y

resultado = somar(2)
print(somar(2))
print(somar(2, 3))

def escopo():
    global variabel_global 
    variabel_global = "Será uma boa prática?"
    print("escopo")

# sem chamar a função a variável não é definida!
escopo()
print(variabel_global)

#### Exceções ####
#a = input("Digite um número:")
#b = input("Digite outro número:")
# try:
#     a = int(a)
#     b = int(b)
# except Exception:
#     print("Deu ruim!")

# try:
#     print(a / b)
# except ZeroDivisionError, ArithmeticError:
#     print("Não é possível dividir por zero.")
# except Exception:
#     print("Deu ruim de novo!")


def add(x, y): 
    """ 
    Returns x + y. 
    :param x: int. 
    :param y: int. 
    :return: int sum of x and y.
    """ 
    return x + y

add(1, 2)

# 1
def numero_ao_quadrado(numero):
    return numero**2
print(numero_ao_quadrado(3))

# 2
def imprimir(texto):
    print(texto)
imprimir("Oii!")

# 3
def exercicio_3(x, y, z, a = 0, b = 0):
    return x + y + z + a + b
print(exercicio_3(1, 2, 3))

# 4
def divide_por_2(x):
    return x / 2

def multiplca_por_4(y):
    return y * 4

resultado = divide_por_2(4)
print(multiplca_por_4(resultado))

# 5
try:
    decimal = float("1.3")
    print(decimal)
except ValueError:
    print("Erro!")

#### Containers ####
print("Texto".upper())
print("Texto".lower().replace("t", "1"))

# Listas
lista = list()
print(lista)
lista = []
print(lista)
lista = [1, 2, 3]
print(lista)
print(lista[0])
print(lista[2])
lista.append(4)
print(lista[3])
lista[0] = "Um"
print(lista)
lista.pop()
print(lista)
print(2 in lista)
print(1 in lista)
print(1 not in lista)
print(len(lista))

# Tuplas
tupla = tuple()
print(tupla)
tupla = ()
print(tupla)
tupla = ("Nome", 2010, True)
print(tupla)
tupla = ("Nome",)
print(tupla)
tupla = ("Nome", 2010, True)
print(tupla[0])
print(tupla[2])
print("Nome" in tupla)
print("Nome" not in tupla)

# Dicionários
dicionario = dict()
print(dicionario)
dicionario = {}
print(dicionario)
dicionario = {"Nome": "Nome"}
print(dicionario)
dicionario = {"id1": "Nome 1", 2: "Nome 2", "id3": "Nome 3"}
print(dicionario)
dicionario["id1"] = "Outro nome"
print(dicionario)
print(dicionario["id3"])
print("id1" in dicionario)
print("id1" not in dicionario)
del dicionario["id1"]
print("id1" in dicionario)
print(dicionario)

# Containers in Containers - Matrizes
lista1 = ["Nome 1", "Nome 2"]
lista2 = [1, 2, 3]
matriz = []
matriz.append(lista1)
matriz.append(lista2)
print(matriz)
print(matriz[0])

# Lista com tupla
lista = ["Primeiro Item"]
tupla1 = ("a1", "a2", "a3")
tupla2 = (1, 2)
lista.append(tupla1)
lista.append(tupla2)
print(lista)

# Tupla com lista
lista1 = [1,2,3]
lista2 = ["Nome 1", "Nome 2"]
tupla = ("1", 1, lista1, lista2)
print(tupla)

# Dicionario com tupla no dicionario
dicionario = {"l1": lista1, "l2": lista2, tupla1: tupla1, "tupla2": tupla2}
print(dicionario)

#### Desafios ####

# 1
musicos = ["Chopin", "Bethoven", "Mozart"]
print(musicos)

# 2 
lugar1 = (23424, 423423)
lugar2 = (2342434, 42342343)
localizacao = [lugar1, lugar2]
print(localizacao)

# 3
preferencias = {"cor": "Roxo", "franquia": "Senhor dos Anéis"}
print(preferencias)

# 4
# print("Qual a sua cor favorita?")
# cor_favorita = input()
# print("Qual a sua franquia favorita?")
# franquia_favorita = input()
# preferencias["cor"] = cor_favorita
# preferencias["franquia"] = franquia_favorita
# print(preferencias)

# 5
musicas = {musicos[0]: ["m1", "m2"], musicos[1]: ["m3, m4, m5"]}
print(musicas)

# 6
# Set é similar ao dicionário, mas não tem chaves, possui valores únicos, não aceita repetições e não é acessível por índices 
# Poderia ser usado para garantir que não hajam repetições de valores sem ser necessário verificar por itens existentes na hora de inserir novos valores
conjunto = {1, 2, 3, 3}
print(conjunto)