"""Variant 2 of word game"""
import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme


console = Console(width=40, theme=Theme({"warning": "red on yellow"}))


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


def show_guess(guesses, word):
   for guess in guesses:
        styled_guess= []
        for letter, correct in zip(guess, word):
            if letter == correct:
               style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

            
        console.print("".join(styled_guess), justify="center")


def game_over(word):
    """Show game over with correct word"""
    print(f"The word was {word}")


def main():
    """The process of our app-flow"""
    # Pre-process
    words_list_path = pathlib.Path('./wordle_v3/wordlist3.txt')
    words_list = [
        word.upper() for word in words_list_path.read_text(encoding="utf-8").split('\n')
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]
    word = get_random_word(words_list)
    guesses = ["_"*5]*6

    # Process (main loop)
    for idx in range(6):
        refresh_page(headline=f"Guess {idx + 1}")
        show_guess(guesses[idx], word)
        

        guesses[idx] = input("\nGuess word: ").upper()
        if guesses[idx] == word:
            break


    # Post-process
    else:
        game_over(word)


if __name__ == "__main__":
    main()
    