"""Variant 2 of word game"""
import pathlib
import random
from string import ascii_letters


def get_random_word(words_list, nr_letters:int=5):
    """Returns: a random word from a list of words

    ### Example:

    >>> get_random_word(["snake", "worm", "apa"], 5)
    'SNAKE'
    """

    words = [
        word.upper()
        for word in words_list
        if len(word) == nr_letters and all(letter in ascii_letters for letter in word)
        ]

    return random.choice(words)


def show_guess(guess, word):
    """Show guessing letters on the terminal and classify all letters

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
        }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

    return correct_letters, misplaced_letters, wrong_letters


def game_over(word):
    """Show game over with correct word"""
    print(f"You guess WRONG, the word was {word}")


def main():
    """The process of our app-flow"""
    # Pre-process
    words_list_path = pathlib.Path('./wordle_v2/wordlist2.txt')
    words_list = [
        word.upper() for word in words_list_path.read_text(encoding="utf-8").split('\n')
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]
    word = get_random_word(words_list)
    print(word)

    # Process (main loop)
    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess=guess, word=word)
        if guess == word:
            print(f"You find the correct word, {word}")
            break


    # Post-process
    else:
        game_over(word)


if __name__ == "__main__":
    main()
    