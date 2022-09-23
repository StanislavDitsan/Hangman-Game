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


"""The user won't get out of the loop until they enter a valid letter."""


def ask_letter():
    chosen_letter = ""
    is_valid = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while not is_valid:
        chosen_letter = input("Please enter a letter!")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")

    return chosen_letter
