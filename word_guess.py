"""
Word Guessing Game
"""

import random
import tkinter

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def main():
    """
    To play the game, first calls the get_word() function to select the secret word for the
    player to guess and then calls the play_game() function to start and play the game with that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


def get_word():
    """
    Selects a word from the file specified by the constant LEXICON_FILE.
    """
    file = open(LEXICON_FILE)
    secret_word_list = []
    for word in file:
        secret_word_list.append(word.strip())
    file.close()

    return random.choice(secret_word_list)


def play_game(secret_word):
    """
    Starts and plays the game until all the 8 guesses are used or the secret word is guessed correctly.
    """
    remaining_guess_count = INITIAL_GUESSES
    hidden_word = len(secret_word) * ['-']
    wrong_letters = []

    while remaining_guess_count != 0 and ''.join(hidden_word) != secret_word:
        print("")
        print("The word now looks like this: " + ''.join(hidden_word))
        print("You have " + str(remaining_guess_count) + " guesses left")
        guess = input("Type a single letter here, then press enter: ")
        upper_guess = guess.upper()

        if len(upper_guess) != 1:
            print("Guess should only be a single character.")
        elif upper_guess in hidden_word:
            print("You have guessed this letter before, try again!")
        elif upper_guess in secret_word:
            print("That guess is correct.")
            for i, letter in enumerate(secret_word):  # Loop through the letters in the secret word
                if upper_guess == letter:             # Check if the current looped letter is equal to the guess
                    hidden_word[i] = letter           # Set the score at that position to the correct letter
        else:
            remaining_guess_count -= 1
            print("There are no " + upper_guess + "'s in the word")
            wrong_letters.append(upper_guess)
            print("You entered these wrong letters until now: " + ', '.join(wrong_letters))

    if remaining_guess_count == 0:
        print("Sorry, you lost. The secret word was: " + secret_word)
    else:
        print("Congratulations, the word is: " + secret_word)


if __name__ == "__main__":
    main()
