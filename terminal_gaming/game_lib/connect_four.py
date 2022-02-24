
from typing import List, Optional
import random

YELLOW = "💩" # 0
RED = "💥" # 1
EMPTY = "_" # None

matrix_t = List[List[Optional[int]]]

def init_matrix(nb_cols: int, nb_rows: int) -> matrix_t:
    return [[None for _ in range(nb_rows)] for _ in range(nb_cols)]

def display_board(matrix: matrix_t) -> None:
    print("\n".join(["".join(["_" for val in matrix]) for i in range(len(matrix[0]))]))
    # for r in range(len(matrix)):
    #     row: List[Optional[int]] = [x for x in matrix[r]]
    #     row: List[str] = [
    #         EMPTY if v == None else (RED if v == 1 else YELLOW) for v in row
    #     ]
    #     print("".join(row))
    # print("".join([str(x+1) for x in range(len(matrix[0]))]))

def get_user_input(matrix: matrix_t) -> int:
    ...

def insert_into_column(
    matrix: matrix_t, 
    selected_column: int, 
    player: int
) -> matrix_t:
    ...

def check_stop_condition(matrix: matrix_t, selected_column: int) -> bool:
    ...

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
        break
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
        player = 0 if player == 1 else 1 # TODO: ternary
        turn_nb += 1









if __name__ == '__main__':
    play()