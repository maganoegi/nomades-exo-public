
from operator import indexOf
from typing import List, Optional
import random

YELLOW = "💩" # 0
RED = "💥" # 1
EMPTY = "_" # None

matrix_t = List[List[Optional[int]]]

class InvalidInputLengthError(Exception):
    """ exception to handle invalid input lengths """


class NotNumericInputError(Exception):
    """ exception to handle numerical inputs instead of characters """


class InvalidColumnNumberError(Exception):
    """ exception to handle numerical inputs instead of characters """


class FullColumnError(Exception):
    """ exception to handle numerical inputs instead of characters """
    message = "the column is full"


def init_matrix(nb_cols: int, nb_rows: int) -> matrix_t:
    return [[None for _ in range(nb_rows)] for _ in range(nb_cols)]

def display_board(matrix: matrix_t) -> None:
    adapted = "\n".join(
        ["".join(
            [
                EMPTY if val[i] == None 
                else (RED if val[i] == 1 else YELLOW) for val in matrix
            ]) for i in range(len(matrix[0])
        )]
    )
    print(adapted)
    print("".join([str(x+1) for x in range(len(matrix))]))

def get_user_input(matrix: matrix_t) -> int:
    while True :
        try:
            char = input("Entrez une colonne : ")

            if len(char) != 1: 
                raise InvalidInputLengthError

            if not char.isnumeric() : 
                raise NotNumericInputError

            if (1 > int(char)) or (int(char) > len(matrix)):
                raise InvalidColumnNumberError

            if matrix[int(char)-1].count(None) == 0:
                raise FullColumnError

            return int(char)

        except NotNumericInputError or InvalidInputLengthError:
            print("Error 1")
            continue

        except InvalidColumnNumberError:
            print("Error 2")
            continue

        except FullColumnError as e:
            print(e.message)
            continue


def insert_into_column(
    matrix: matrix_t, 
    selected_column_nb: int, 
    player: int
) -> matrix_t:
    #rev = reversed(selected_col)
    #rev = selected_col[::-1]

    selected_col = list(reversed(matrix[selected_column_nb-1]))
    matrix[selected_column_nb-1][len(matrix[0])-1-indexOf(selected_col, None)] = player

    return matrix

def check_stop_condition(
    matrix: matrix_t, 
    selected_column: int, 
    player: int
) -> bool:
    return 

def play() -> None:
    NB_COL = 7
    NB_ROW = 6
    MAX_TURNS = NB_COL * NB_ROW
    turn_nb = 0

    matrix = init_matrix(nb_cols=NB_COL, nb_rows=NB_ROW)

    player = random.randint(0, 1)
    is_running = True
    while is_running:
        display_board(matrix)
        
        # ask the client number what column he would like to play
            # check whether the choice is valid
        selected_column = get_user_input(matrix)

        # insert the number into the column
        matrix = insert_into_column(matrix, selected_column, player)

        # check whether player has won OR matrix full
        is_running = check_stop_condition(
            matrix, 
            selected_column, 
            turn_nb
        )

        # switch players
        player = 0 if player == 1 else 1
        turn_nb += 1

if __name__ == '__main__':
    play()