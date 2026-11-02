###### 1. Primeiro Programa ######

print("Olá, mundo!")
print("Olá, Giu!")

# Imprime olá 10x
for i in range(10):
    print("Olá, mundo!")

# Texto em múltiplas linhas
print("""
    Esse
    texto
    tem
    5
    linhas.
""")

# Identação obrigatória ao invés de brackets

###### 2. Sintaxe ######

# Tipos de Dados: 
# Ex: “Olá”: data type: str, value: “Olá”
texto = "Olá"
print(texto)

# Ex: 1: data type: int, value: 1
inteiro = 1 + 2
print(inteiro)

# Ex: 1.2: data type: float, value: 1.2
decimal = 1.2 + 1.2
print(decimal)

# Ex: True ou False: data type: bool, value: True ou False
print(True)
print(False)

# Ex: None: data type: None, value: ausência de valor
print(None)

###### 3. Tipos e Variáveis ######

# Constantes: ex: números
print(1 + 3)
print(4 - 2)

## Variáveis - no python não especifica o tipo da variável
numero = 1
print(numero)
numero = 2
print(numero)

a = 1
b = 2
print(a + b)

a -= 1
b += 1

print(a)
print(b)

ola = "Olá!"
print(ola)

# Código com erro de sintaxe - descomentar para ver mensagem de erro
# erro = "String incompleta

# Código com exceção - descomentar para ver mensagem de erro
# divisao_por_zero = 1/0

###### 4. Operadores ######

## Aritméticos
print(2 ** 2) # Potenciação
print(14 % 4) # resto da divisão / módulo
print(13 // 8) # valor inteiro da divisão
print(13 / 8) # divisão
print(8 * 2) # multiplicação
print(7 - 1) # subtração
print(2 + 2) # adição

# Precedência
print (2 + 2 * 2)
print ((2 + 2) * 2)

## Comparação - retornam valores booleanos
print(1 >= 2)
print(3 >= 2)
print(2 == 2)
print(2 != 2)

## Lógicos - retornam valores booleanos
print(1 == 1 and 2 == 3)
print(1 == 1 or 2 == 3)
print(1 == 1 or 2 == 3 or 1 == 3)
print(not 1 == 1 or 2 == 3 or 1 == 3)

###### 5. Condicionais ######

if (1 == 1):
    print("1 == 1")
else:
    print("1 != 1")

if (2 == 3):
    print("2 == 3")
else:
    print("2 != 3")

if (4 == 3):
    print("4 == 3")
elif (4 == 5):
    print("4 == 5")
else:
    print("4 != 3 and 4 != 5")

# Desafios

print("1")
print("2")
print("3")

number = 9
if (number < 10):
    print("menor que 10")
else:
    print("maior ou igual a 10")


number = 26
if (number <= 10):
    print("menor que 10")
elif (10 < number <= 25):
    print("maior que 10 e menor ou igual a 25")
else:
    print("maior que 25")

a = 10
b = 3

print(a % b)

a = 8
b = 4

print(a/b)

age = 17
if (age < 18):
    print("menor de idade")
else:
    print("maior de idade")


age = 18

if (age < 18):
    print("menor de idade")
else:
    print("maior de idade")

print(age)

age = "teste"
print(age)