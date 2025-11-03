import pytest
import guess_the_word

def test_choose_random_word():
    words = ["python", "student", "computer"]
    selected = guess_the_word.choose_random_word(words)
    # Check that chosen word is from predefined list
    assert selected in words

def test_process_guess_correct():
    rand = "python"
    guessed = set()
    result = guess_the_word.process_guess(rand, guessed, "p")
    # Correct guess should return True and add the letter
    assert result is True
    assert "p" in guessed

def test_process_guess_incorrect():
    rand = "python"
    guessed = set()
    result = guess_the_word.process_guess(rand, guessed, "z")
    # Incorrect guess should return False and add the letter
    assert result is False
    assert "z" in guessed
