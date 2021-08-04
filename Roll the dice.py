import random

Dice= random.randint(1,6)

print(Dice)

while Dice==6:
    print("you get the six lucky one another turn is your prize")
    Dice = random.randint(1, 6)
    print(Dice)
