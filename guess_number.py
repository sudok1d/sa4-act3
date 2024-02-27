number = 10

print("I'm thinking of a number...")
counter = 3
while counter > 0:
    guess = input("What number am I thinking of? ")
    counter -= 1

    if guess == 'q':
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print(f"You guessed too high. \nYou now have {counter} guesses left.")
    else:
        print(f"You guessed too low. \nYou now have {counter} guesses left.")
    
print(f"The number was {number}")
    