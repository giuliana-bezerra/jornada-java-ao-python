#### Strings ####
print("""
    essa é
    uma string
    em várias linhas
""")

nome = "giuliana"
print(nome[0])
print(nome[7])
print(nome[-1])
print(nome[-2])

nome_completo = "Giuliana " + "Bezerra"
print(nome_completo)
print(nome_completo * 3)
print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.lower())
print("giuliana bezerra".capitalize())

#### Formatação ####
print("Meu nome é {}".format(nome_completo))
print("Primeira frase. Segunda frase".split("."))
print("+".join("12345"))
palavras = ["Uma", "frase", "aleatória", "."]
print("".join(palavras))
print(" teste ".strip())
print("Andar pensar correr dormir".replace("a", "@"))
try:
    print("Giuliana".index("a"))
except:
    print("Not found.")

print("giu" in "Um dois três giu quatro")
print("giu" not in "Um dois três giu quatro")
print("Foi utiliza a palavra \"árvore\"")
print('Foi utiliza a palavra "árvore"')
print("Linha 1\Linha 2")
brinquedos = ["Boneca", "Urso", "Bola"]
print(brinquedos[0:1])
print("Giuliana Bezerra"[0:3])
print("Giuliana Bezerra"[:3])
print("Giuliana Bezerra"[9:])
print("Giuliana Bezerra"[:])

#### Challenges ####
# 1
print(" ".join("Camus"))

# 2
# print("Response 1: ")
# response1 = input()
# print("Response 2: ")
# response2 = input()
# print("Yesterday I wrote a {}. I sent to {}".format(response1, response2))

# 3
print("aldous Huxley was born in 1894".capitalize())

# 4
questions = "Where now? Who now? When now?".split("?")
print(questions)

# 5
print(" ".join(["The", "fox", "jumped", "over", "the", "fence", "."])[:-2] + ".") 

# 6
print("A screaming comes across the sky.".replace("s", "$"))

# 7
print("Heming-way".index("m"))

# 8
print('He said, "How can I help you?"')

# 9
print("three " + "three " + "three")
print("three " * 3)

# 10
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
print(sentence[:sentence.index(",")])


#### For ####
name = "Giuliana"
for character in name:
    print(character)

lista = [1, 2, 3, "Quatro"]
for elemento in lista:
    print(elemento)

tupla = ("Valor 1", "Valor 2", "Valor 3")
for elemento in tupla:
    print(elemento)

dicionario = {"chave1": "valor 1"}
for chave in dicionario:
    print(chave)

for i in range(0,100):
    print(i)
    break

for i in range(1, 10):
    if i == 3:
        continue
    print(i)

lista = [1, 2, 3]
for index, elemento in enumerate(lista):
    print(index, elemento)

for i in range(1, 11):
    print(i)

x = 10
while x > 0:
    print(x)
    x -= 1

while input('y or n?') != 'n':
    print("Yes")

### Challenges ####
# 1.
tv = [ "The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for item in tv:
    print(item)
# 2.
for i in range(25, 50):
    print(i)
# 3.
for index, item in enumerate(tv):
    print(index, item)
# 4.
numbers = [2, 5, 8]
while True:
    print("Chute um número ou 'q' para sair:")
    number = input()
    if number == "q":
        break
    
    if int(number) in numbers:
        print("Acertou")
    else:
        print("Errou!")

# 5.
lista1 = [8, 19, 148, 4]
lista2 = [9, 1, 33, 83]
lista3 = []

for numero_lista1 in lista1:
    for numero_lista2 in lista2:
        lista3.append(numero_lista1 * numero_lista2)
print(lista3)