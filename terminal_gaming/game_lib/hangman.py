

import random
from typing import List, Tuple, Optional

HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ==='''
]

WORDS = [
    "python",
    "iterator",
    "generator",
    "mutability",
    "abstraction",
    "nomades",
    "classmethod"
]

WIN_PROMPT = "YOU HAVE WON !!!"
LOSE_PROMPT = "YOU HAVE LOST !!!"
HIDDEN = "_"

class InvalidInputLengthError(Exception):
    """ exception to handle invalid input lengths """
# 2 espaces entre les classes, sinon 1

class NumericInputError(Exception):
    """ exception to handle numerical inputs instead of characters """


def get_user_input():
    while True :
        try:
            char = input("Entrez un caractère : ")

            if len(char) != 1: 
                raise InvalidInputLengthError

            if char.isnumeric() : 
                raise NumericInputError

            return char.lower()

        except InvalidInputLengthError as e:
            print("Length should be 1")
            continue

        except NumericInputError as e:
            print("[]aA-zZ] authrized")
            continue
 
def get_letter_occurences_in_word(letter, word):
    # [operation for declaration in collection if condition]
    return [i for i, val in enumerate(word) if letter == val]

def write_letter_in_hidden_word(hidden_word: str, letter: str, indices: List[int]) -> str:
    return "".join(
        [letter if i in indices else val for i, val in enumerate(hidden_word)]
    )

def play():
    error_cnt = 0
    done = False

    selected_word = random.choice(WORDS).lower()

    hidden_word = HIDDEN * len(selected_word) # attention pour les mutables!
    # list(str) -> str : "delim".join(lst of strings)
    # hidden_word = "".join(["_" for _ in range(len(selected_word))]) 
    while not done:

        print(hidden_word)
        letter = get_user_input()

        is_letter_in_word = letter in selected_word
        is_letter_opened = letter in hidden_word


        if is_letter_in_word:
            if not is_letter_opened:
                indices = get_letter_occurences_in_word(letter, selected_word)

                hidden_word = write_letter_in_hidden_word(hidden_word,letter,indices)

            else:
                continue

        else:
            print(HANGMAN_PICS[error_cnt])
            error_cnt += 1

        winning_condition = hidden_word == selected_word
        losing_condition = error_cnt == len(HANGMAN_PICS)

        if winning_condition or losing_condition:
            print(WIN_PROMPT if winning_condition else LOSE_PROMPT)
            done = True


if __name__ == '__main__':
    # quand le script est execute "directement"
    # permet aussi de tester sans tests unitaires, rapidement
    play()


