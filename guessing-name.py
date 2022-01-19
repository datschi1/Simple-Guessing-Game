import random 
import turtle

secretNumber = random.randint(0,1000)
points = 0

while True:
    x = int(input("Guess the Number: "))
    points = points + 1
    if x > secretNumber:
        print("Lower")
    elif x < secretNumber:
        print("Higher")
    else:
        print("You Won!")
        print(f"It took you {points} Tries")
        break

