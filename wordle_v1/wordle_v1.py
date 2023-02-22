"""Variant 1 of word game"""
import pathlib
import random
from string import ascii_letters

# print(pathlib.Path('./wordle_v1/wordlist.txt').read_text(encoding="utf-8"))
words_list_path = pathlib.Path('./wordle_v1/wordlist2.txt')
words_list = [
    word.upper() for word in words_list_path.read_text(encoding="utf-8").split('\n')
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]


word = random.choice(words_list)
print(word)


for guess_num in range(1,7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == word:
        print("Correct")
        break

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
        }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)


    print("Correct letters: ", ", ".join(sorted(correct_letters)))
    print("Misplaced letters: ", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters: ", ", ".join(sorted(wrong_letters)))


else:
    print(f"You guess WRONG, the word was {word}")
    