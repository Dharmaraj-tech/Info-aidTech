import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")

    play_again = True

    while play_again:
        secret_number = random.randint(1, 100)
        attempts = 0
        guess = None

        while guess != secret_number and attempts < 10:
            try:
                guess = int(input("Enter your guess (between 1 and 100): "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                attempts += 1

                if guess < secret_number:
                    print("Too low! Try a higher number.")
                elif guess > secret_number:
                    print("Too high! Try a lower number.")
                else:
                    print(f"Congratulations, {name}! You guessed the number {secret_number} in {attempts} attempts.")
                    break

                if attempts == 10:
                    print(f"Sorry, {name}. You've reached the maximum number of attempts. The number was {secret_number}.")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        play_choice = input("Do you want to play again? (yes/no): ").lower()
        if play_choice != 'yes':
            play_again = False
            print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    number_guessing_game()
