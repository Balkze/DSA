import random

def game():
    number_to_guess = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    count=0
    while guess != number_to_guess:
        if guess < number_to_guess:
            print("Too low!")
            count+=1
        else:
            print("Too high!")
            count+=1
        guess = int(input("Guess again: "))
        
    print("Congratulations! You guessed the number.")

game()
