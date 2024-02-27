number = 10

print("I'm thinking of a number...")
while True:
    guess = input("What number am I thinking of? ")

    if guess == 'q':
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print("You guessed too high.")
    else:
        print("You guessed too low.")
    

    