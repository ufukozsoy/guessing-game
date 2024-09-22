import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()

