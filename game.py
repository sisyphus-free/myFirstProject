import random

MAX_NUMBER = 20
MAX_ATTEMPTS = 5


def read_guess(min_number: int, max_number: int) -> int:
    """Read and validate a player's guess."""
    while True:
        raw_value = input("Enter your guess: ")

        if not raw_value.strip().isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw_value)
        if guess < min_number or guess > max_number:
            print(f"Your guess must be between {min_number} and {max_number}.")
            continue

        return guess


def compare_guess(guess: int, secret_number: int) -> str:
    """Return feedback about the guess."""
    if guess < secret_number:
        return "too low"
    if guess > secret_number:
        return "too high"
    return "correct"


def play_game() -> None:
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number from 1 to {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")

    secret_number = random.randint(1, MAX_NUMBER)
    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        print(f"Attempts left: {attempts_left}")
        guess = read_guess(1, MAX_NUMBER)
        result = compare_guess(guess, secret_number)

        if result == "correct":
            print(f"Great job! You guessed the number: {secret_number}")
            return

        print(f"Your guess is {result}. Try again.\n")
        attempts_left -= 1

    print(f"Out of attempts! The secret number was {secret_number}.")


if __name__ == "__main__":
    play_game()
