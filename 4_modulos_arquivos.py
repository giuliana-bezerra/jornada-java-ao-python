#### Modules ####
import math
import random
import statistics
import keyword
import modules.module1
import modules.cube as cube

print(math.pow(2, 3))
print(random.randint(1,10))
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("for2"))

#### Challenges ####
# 1
print(statistics.cos(180))
# 2
print(cube.cube(2))

#### Files ####
import os
file = os.path.join(".", "teste.txt")
# st = open(file, "w")
# st.write("Hi from python!")
# st.close

with open(file, "w") as f:
    f.write("Hi again!\n")
    f.write("Hi again 2!\n")
    f.write("Hi again 3!\n")

lines = []
with open(file, "r") as f:
    lines.append(f.read())

print(lines)

#### CSV Files ####
import csv

with open("teste.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["1", "2", "3"])
    w.writerow(["4", "5", "6"])

with open("teste.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

#### Challenges ####
# 1
file = os.path.join(".", "file.txt")
print(file)

with(open(file, "r")) as f:
    print(f.read())

# 2
# print("Qual o seu file favorito?")
# answer = input()

# file = os.path.join(".", "answer.txt")
# with(open(file, "w")) as f:
#     f.write(answer)

# 3
movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with (open("movies.csv", "w")) as f:
    w = csv.writer(f, delimiter=",")
    w.writerows(movies)
