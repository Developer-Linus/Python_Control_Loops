# Import the random module
import random # The module facilites generation of random numbers

def play_game():
    # Generate a secret number and store it in secret_number
    secret_number = random.randint(1, 10)

    # User guesses a number
    guess = int(input("Guess a number in the range between 1 and 10: "))

    # Matching user guess with various patterns
    match guess:
        case guess if guess == secret_number:
            print("Congratulations, you guessed it!")
        case guess if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
        case guess if guess>secret_number:
            print("Oops, your guess is a bit high. Try again!")


play_game()

offer_play = input("Do you want to play again? (yes or no): ").lower()
if offer_play == "yes":
    play_game()
else: 
    print("Thanks for your time in trying the challenge. See you next time!")

play_game()
    




