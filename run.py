from random import choice

words = [
    "zombie",
    "adoption",
    "confront",
    "process",
    "establish",
    "head",
    "worth",
    "kidney",
    "mole",
    "tablet",
]
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

"""This function will make the system choose a random word from the list."""


def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters
