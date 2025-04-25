from random import randint

x = randint(range(1, 100))
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100.")
for _ in range(5):
    try:
        y = int(input("What is the number? "))
        if y == x:
            print("You win!")
            break
        elif y < x:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a number betweeen 1 and 100.")
print("Thank you for playing! The game is over.")
