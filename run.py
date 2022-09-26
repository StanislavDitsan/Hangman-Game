from random import choice
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hangman Game!!")
print(ascii_banner)

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

""" User name input - accepts only letters"""
name_input = ""

while True:
    name_input = input("Enter Your Name: ")

    if not name_input.isalpha():
        print("Enter only Letters!\n")
        continue
    else:
        break

print("\nHello", name_input, "\nWelcome to Hangman Game!\n")
print("Try to guess the word in under six attempts!")
print("---------------------------------------------")


def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print(" O--\|")
        print("/|\  |")
        print("/ \  |")
        print("    ===\n")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===\n")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===\n")
    elif wrong == 3:
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===\n")
    elif wrong == 2:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===\n")
    elif wrong == 1:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===\n")


"""This function will make the system
choose a random word from the list."""


def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters


"""The user won't get out of the loop
until they enter a valid letter."""


def ask_letter():
    chosen_letter = ""
    is_valid = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while not is_valid:
        chosen_letter = input("Please enter a letter: ")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")

    return chosen_letter


"""Replacing each letter with a dash so
that the user has to guess which letter
goes on each dash."""


def show_new_board(choose_word):
    hidden_list = []

    for letter in choose_word:
        if letter in correct_letters:
            hidden_list.append(letter)
        else:
            hidden_list.append("-")

    print(" ".join(hidden_list))


"""Checking if the letter the user entered
matches with the hidden word. And every
time the function checks, it will complete
the list of correct and incorrect words.
This function will also check if the user has one try or less."""


def check_letter(chosen_letter, hidden_word, tries, matches):
    end = False

    if chosen_letter in hidden_word and chosen_letter not in correct_letters:
        correct_letters.append(chosen_letter)
        matches += 1
    elif chosen_letter in hidden_word and chosen_letter in correct_letters:
        print("You have already found that letter, try with another one")
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1
        print_hangman(tries)

    if tries == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return tries, end, matches


def lose():
    print("You dont have any tries left\n")
    print("GAME IS OVER!\n")
    print("The hidden word was:" " " + word)

    return True


def win(revealed_word):
    show_new_board(revealed_word)
    print("Congratulations, you guessed the word!")

    return True


word, unique_letters = choose_word(words)


"""Calling the functions by Joining the functions"""

while not game_over:
    print("\n" + "^" * 20 + "\n")
    show_new_board(word)
    print("\n")
    print("Incorrect letters: " + "-".join(incorrect_letters))
    print(f"You have {tries} tries left")
    print("\n" + "^" * 20 + "\n")
    letter = ask_letter()
    tries, over, right_answers = check_letter(
        letter, word, tries, right_answers)
    game_over = over
