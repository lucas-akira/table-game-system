from boardgame import BoardGame
from action import Action
from turn import Turn


def list_options():
    print("1: Create a new game")
    print("2: Start a new game")
    print("3: Exit")


def positive_int_input():
    repeat = True
    while repeat:
        receiver = input()
        repeat = False
        try:
            receiver = int(receiver)
            if receiver <= 0:
                print("Please enter a positive integer!")
                repeat = True
        except ValueError:
            print("Please enter an integer!")
            repeat = True
    return receiver


def int_input_greater_than_one():
    repeat = True
    while repeat:
        receiver = positive_int_input()
        repeat = False
        if receiver <= 1:
            print("Please enter an integer greater than 1!")
            repeat = True

    return receiver


def create_game_menu():
    repeat = True
    while repeat:
        print("Choose a name for the game:")
        name = input()

        print("Height of the grid:")
        height = int_input_greater_than_one()

        print("Width of the grid:")
        width = int_input_greater_than_one()

        print("Number of players:")
        number_players = positive_int_input()

        piece_markers = []
        print("How many types of pieces?")
        number_types_pieces = positive_int_input()

        for i in range(number_types_pieces):
            print("Marker of piece number {}: (it can't be 0)".format(i+1))
            need_to_ask = True
            while need_to_ask:
                marker = input()
                if marker != "0":
                    need_to_ask = False
                    piece_markers.append(marker)
                else:
                    print("Marker can't be 0! Try again")
                    need_to_ask = True
        print("Verify win every turn? (y or n)")
        end_type=input()
        print("Length to win:")
        length_to_win = positive_int_input()

        print("-------------------------------------")
        print("Recap: ")
        print("Name: {}".format(name))
        print("Grid height: {}".format(height))
        print("Grid width: {}".format(width))
        print("Pieces:")
        print("End type: {}".format(end_type))
        print("Length to win: {}".format(length_to_win))
        for i in range(number_types_pieces):
            print("  Piece number {}: {}".format(i+1, piece_markers[i]))

        print("Everything OK so far? ")
        print("1: Yes, proceed")
        print("2: No, start over again")
        print("3: Go back to menu")
        option = input()

        if option == "1":
            print("Continuing...")
            board = BoardGame(name, height, width, number_players, piece_markers,end_type,length_to_win)
            actions = add_turn_actions(board.grid)

            if actions is not None:
                # Instanciate a turn
                turn = Turn()
                turn.actions = actions
                ##### after an action, define game over conditions

                for action in actions:
                    print("Action: {} with description: {}".format(action.keyboard_input, action.description))

            repeat = False
        elif option == "2":
            repeat = True
        elif option == "3":
            repeat = False
    return board, actions

def add_turn_actions(grid):
    print("What should each player generally do in their turn?")
    print("1: Try to move all the pieces in the grid in a general position, summing common ones (e.g: 2048)")
    print("2: Add individual pieces in empty spaces (e.g: tic-tac-toe)")
    print("3: Go back to menu")
    option = input()
    actions = []
    if option == "1":
        print("Select which keyboard button will correspond ")
        # Instanciate an action
        action = Action("a", "Move left", ["move_grid"], grid = grid, direction = "left")
        # Put it in the list of actions
        actions.append(action)
        # Repeat for each direction
        action = Action("w", "Move up", ["move_grid"], grid = grid, direction = "up")
        actions.append(action)

        action = Action("d", "Move right", ["move_grid"], grid = grid, direction = "right")
        actions.append(action)

        action = Action("s", "Move down", ["move_grid"], grid = grid, direction = "down")
        actions.append(action)

        return actions

    elif option == "2":
        print("Option 2")
        return None
    elif option == "3":
        return None


def start_menu():
    menu_loop = True
    while menu_loop:
        print("__Board Game__")
        list_options()
        print("Choose an option:")
        option = input()

        if option == "3":
            menu_loop = False
        elif option == "2":
            # Start created game
            print("Option 2")
        elif option == "1":
            turn = create_game_menu()
        else:
            print("Invalid option! Try again!")


start_menu()
