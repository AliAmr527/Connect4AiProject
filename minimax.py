import copy

EMPTY = 0
RED = 1
BLUE = 2
WIN_SCORE = 1000000000


# Minimax with alpha-beta pruning
def minimax(board, depth, maximizingPlayer):
    game_board, game_end = copy.deepcopy(board.get_game_grid())
    # Check if the game has ended, or we have reached the maximum depth
    if game_end or depth == 0:
        return None, evaluate_board(copy.deepcopy(game_board))

    if maximizingPlayer:
        max_score = -WIN_SCORE
        best_column = None
        for column in range(7):
            if is_valid_move(game_board, column):
                game_board = make_move(copy.deepcopy(game_board), copy.deepcopy(column), RED)
                _, score = minimax(copy.deepcopy(board), depth - 1, False)
                if score > max_score:
                    max_score = score
                    best_column = copy.deepcopy(column)
        return best_column, max_score
    else:
        min_score = WIN_SCORE
        best_column = None
        for column in range(7):
            if is_valid_move(game_board, column):
                game_board = make_move(copy.deepcopy(game_board), copy.deepcopy(column), BLUE)
                _, score = minimax(copy.deepcopy(board), depth - 1, True)
                if score < min_score:
                    min_score = score
                    best_column = copy.deepcopy(column)
        return best_column, min_score


# Check if the move is valid
def is_valid_move(board, column):
    return board[0][column] == EMPTY


# Make a move on the board
def make_move(board, column, player):
    new_board = [row[:] for row in board]
    for i in range(5, -1, -1):
        if new_board[i][column] == EMPTY:
            new_board[i][column] = player
            break
    return new_board


# Evaluate the board

