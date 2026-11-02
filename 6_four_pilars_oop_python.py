#### Encapsulamento ####
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = "unsafe"

    def public_method(self):
        print("safe")

    def _private_method(self):
        print("unsafe")

obj = PublicPrivateExample()
print(obj.public)
obj.public_method()

#### Abstração e Polimorfismo ####
class Triangle:
    def draw(self):
        print("Triangle")

class Circle:
    def draw(self):
        print("Circle")


shapes = [Triangle(), Circle()]
for shape in shapes:
    shape.draw()

#### Herança ####
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
        """.format(self.width, self.len))

class Square(Shape):
    pass

square = Square(20, 20)
square.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}
        """.format(self.width, self.len))

square = Square(20, 20)
print(square.area())
square.print_size()

#### Composição ####
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)

#### Desafios ####
# 1, 2, 3
class Shape:
    def what_am_i(self):
        print("I'm a shape")

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    def calculate_perimeter(self):
        return (self.height * 2) + (self.weight * 2)

    def what_am_i(self):
        print("I'm a Rectangle")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, number):
        self.side = self.side - number

    def what_am_i(self):
        print("I'm a Square")

square = Square(2)
rectangle = Rectangle(2, 4)

print(square.calculate_perimeter())
print(rectangle.calculate_perimeter())
square.change_size(1)
print(square.calculate_perimeter())
square.what_am_i()
rectangle.what_am_i()

# 4
class Horse:
    def __init__(self, rider):
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

horse = Horse(Rider("Tom"))

print(horse.rider.name)