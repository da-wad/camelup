import random

def get_dice_number():
    return random.randint(1,3)

def get_dice_colours():
    colours = ["RED", "YELLOW", "GREEN", "BLUE", "PURPLE"]
    return random.sample(colours, len(colours))

def get_dice_with_numbers():
    return [(colour, get_dice_number()) for colour in get_dice_colours()]

def create_game_board():
    return [[] for n in range(16)]

def initialize_game_board():
    game_board = create_game_board()
    first_dice_rolls = get_dice_with_numbers()
    for roll in first_dice_rolls:
        game_board[roll[1] - 1].append(roll[0])
    return game_board
    
def get_camel_position(game_board, colour):
    for i, square in enumerate(game_board):
        if colour in square:
            return i + 1


def advance_camels(game_board, n_rolls, verbose=False):
    dice_rolls = get_dice_with_numbers()
    for roll in dice_rolls:
        n_rolls += 1
        if verbose:
            print(game_board)
            print("Roll #{} = {}".format(n_rolls, roll))
        square_id = get_camel_position(game_board, roll[0])
        square = game_board[square_id - 1]
        moving_camels = square[square.index(roll[0]):]
        game_board[square_id - 1] = square[:len(square) - len(moving_camels)]
        if square_id + roll[1] - 1 > 15:
            return True, n_rolls, moving_camels[-1]
        game_board[square_id + roll[1] - 1] = game_board[square_id + roll[1] - 1] + moving_camels
    return False, n_rolls, None

def play_game():
    game_board = initialize_game_board()
    n_rolls = 0
    finished = False
    while not finished:
        finished, n_rolls, winner = advance_camels(game_board, n_rolls)
    return winner, n_rolls, game_board

if __name__ == "__main__":
    winner, n_rolls, final_game_board = play_game()
    print(winner, "Wins")
    print("Game took {} rolls.".format(n_rolls))
    print("Final positions: {}".format(final_game_board))
