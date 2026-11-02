#### OO ####
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(10, "Orange")
print(orange)
print(orange.color)
print(orange.weight)
orange.rot(10, 98)
print(orange.mold)

#### Desafios ####
# 1
class Apple:
    def __init__(self, color, weight, apple_type, size):
        self.color = color
        self.weight = weight
        self.apple_type = apple_type
        self.size = size
a1 = Apple("red", 2, "fuji", "small")
a2 = Apple("pink", 3, "red", "regular")
a3 = Apple("red", 4, "gala", "regular")
a4 = Apple("red", 5, "red", "big")

# 2
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(self.radius * (math.pi ** 2))

circle = Circle(2)
circle.area()

## 3
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2

triangle = Triangle(10, 6)
print(triangle.area())

## 4 
class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

h = Hexagon(4)
print(h.calculate_perimeter())
