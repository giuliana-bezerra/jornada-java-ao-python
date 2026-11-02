# type hints
from dataclasses import dataclass, field


def calcularTotal(preco: float, quantidade: int) -> float:
    return preco * quantidade


print(calcularTotal("wef", 3))  # funciona :O
print(calcularTotal(1, 3))  # funciona :O
print(calcularTotal(1.1, 3))  # funciona :)

nome: str = "Giuliana"  # variáveis
nomes: list[str] = ["str1", "str2"]
notas: dict[str, float] = {
    "Giuliana": 10.0
}


def buscar_usuario(id: int) -> str | None:
    if id == 1:
        return "Giu"
    return None


# Dataclasses
@dataclass(repr=True, eq=True)  # Para imutável (frozen=True)
class Cliente:
    nome: str
    email: str
    ativo: bool = True  # últimos na ordem
    idade: int = 0
    enderecos: list[str] = field(
        default_factory=list, repr=False)  # não usar []

    def __post_init__(self):
        if not isinstance(self.idade, (int)):
            raise TypeError("A idade deve ser inteira")


cliente1 = Cliente("Giuliana", "giuliana@email.com")
cliente2 = Cliente("Giuliana", "giuliana@email.com")
print(cliente1)
print(cliente1 is cliente2)
print(cliente1 == cliente2)
cliente1.nome = "G B"
print(cliente1)

# Duck Typing e Protocols

class Cachorro:
    def emitir_som(self):
        print("Au au!")

class Pato:
    def emitir_som(self):
        print("Quack!")

class Pedra:
    pass

def fazer_barulho(animal):
    animal.emitir_som()

fazer_barulho(Cachorro())
fazer_barulho(Pato())
# fazer_barulho(Pedra()) # Erro!

from typing import Protocol

class AnimalSonoro(Protocol):
    def emitir_som(self) -> None:
        pass

def fazer_barulho_protocol(animal: AnimalSonoro) -> None:
    animal.emitir_som()

fazer_barulho_protocol(Cachorro())
fazer_barulho_protocol(Pato())
# fazer_barulho_protocol(Pedra()) # erro!

# Pythonic code
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
 
nomes = ["ana", "bruno", "carla"]

nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)

nomes = ["Ana", "Bruno"]

if nomes:
    print("Existem nomes cadastrados")

if not nomes:
    print("A lista está vazia")

nome, idade = ("Ana", 30)

print(nome)
print(idade)

a = 10
b = 20

a, b = b, a
print(a, b)

primeiro, segundo, *restante = [10, 20, 30, 40, 50]

print(primeiro)   # 10
print(segundo)    # 20
print(restante)   # [30, 40, 50]


numeros = [3, 8, -2, 10]
tem_negativo = any(numero < 0 for numero in numeros)
todos_positivos = all(numero > 0 for numero in numeros)

print(tem_negativo, todos_positivos)

configuracao = {
    "ambiente": "producao",
    "timeout": 30,
}
retries = configuracao.get("retries", 3) # não dá KeyError se não existir a chave