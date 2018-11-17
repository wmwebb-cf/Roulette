import random

dice_one = random.randint(0, 36)

listy = []
for n in range(0, 37):
  listy.append(n)

table = [0, 1, 2, 3, 4, 22, 23, 24, 25]

ball = random.choice(table)
print(listy)
print(ball)
