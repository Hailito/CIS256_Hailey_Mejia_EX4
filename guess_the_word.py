import random

def choose_random_word(words):
    """Select a random word from a predefined list."""
    return random.choice(words)

def process_guess(secret_word, guessed_letters, guess):
    """Return True if guess is correct, otherwise False."""
    guessed_letters.add(guess)
    return guess in secret_word


def word_guessing_game():
    words = [
        "Purple",
        "Dalmation",
        "Blanket",
        "Kitchen",
        "Goat",
        "King",
        "Raccoon",
        "Cake",
        "Trash"
        ]
    rand_word = random.choice(words)
    guessed_letters = set()
    attempts = 10

    print("Welcome to the Word Guessting Game")
    print("You have {attempts} to guess the word.")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in rand_word])
        print(f"\nWord: {display_word}")

        if display_word == rand_word:
            print("Congratulations - You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)

        if guess in rand_word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} left.")

    else:
        print(f"\nGame over! The word was '{rand_word}'.")


if __name__ == "__main__":
    word_guessing_game()
