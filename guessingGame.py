import random
number = random.randint(1,9)
chances=0
print("Number Guessing Game")

while chances<5:
    guess=int(input("Guess a Number between 1 and 9 -> "))
    if guess == number: 
        print("You Won!")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    chances=chances+1
if chances>5:
    print("You Lost :(")

