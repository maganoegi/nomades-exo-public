


from game_lib.game_factory import GAME_FACTORY_DICT


def get_user_game_selection():
    game_name_list = GAME_FACTORY_DICT.keys()
    indexed_game_str = "\n".join([
        f"{index+1}. {name}" for index, name in enumerate(game_name_list)
    ]) 
    PROMPT = "select your game:\n" + indexed_game_str + "\n"

    while True:       
        user_selection = input(PROMPT)
        if (user_selection == 'q'):
            exit(0)

        if (user_selection.isnumeric() and
            0 < int(user_selection) <= len(game_name_list)):
            return GAME_FACTORY_DICT[
                list(game_name_list)[int(user_selection)-1]
            ]
        # try:
        #     user_selection = int(input(PROMPT))
        #     if user_selection == '0':
        #           exit(0)
        #     if (0 < user_selection <= len(game_name_list)):
        #         return GAME_FACTORY_DICT[list(game_name_list)[user_selection-1]]
        # except ValueError:
        #     print("Incorrect value. Should be between 1 and " +  
        #     str(len(game_name_list)) +"\n")
        #     continue


if __name__ == '__main__':
    selected_game = get_user_game_selection()
    selected_game.play()