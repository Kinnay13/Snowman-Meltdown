"""Main game logic for the Snowman Meltdown game."""

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Returns True if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    """Runs the Snowman Meltdown game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):

        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess not in guessed_letters:
            if guess in secret_word:
                guessed_letters.append(guess)
            else:
                mistakes += 1

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
    else:
        print("The snowman melted! The word was:", secret_word)


def ask_replay():
    """Asks the user if they want to play again."""
    while True:
        answer = input("Do you want to play again? (y/n): ").lower().strip()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    while True:
        play_game()
        if not ask_replay():
            print("Thanks for playing!")
            break
