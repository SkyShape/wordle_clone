"""TDD - unittest """
import wordle_v2


def test_get_random_word():
    """Test that a random word from the word list is chosen. """
    word_list = ["SNAKE", "CRANE", "WYRDL"]
    assert wordle_v2.get_random_word(word_list) in word_list


def test_show_guess():
    """Test showing guessing letters on the terminal and classify all letters. """
    guess = "CRANE"
    word = "SNAKE"
    assert wordle_v2.show_guess(guess, word) == ({'A', 'E'}, {'N'}, {'C', 'R'})
