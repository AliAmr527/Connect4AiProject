import copy

EMPTY = 0
RED = 1
BLUE = 2
WIN_SCORE = 1000000000


# Minimax with alpha-beta pruning
def alphabetapruning(board, depth, alpha, beta, maximizingPlayer):
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
                _, score = alphabetapruning(copy.deepcopy(board), depth - 1, alpha, beta, False)
                if score > max_score:
                    max_score = score
                    best_column = copy.deepcopy(column)
                alpha = max(alpha, max_score)
                if beta <= alpha:
                    break
        return best_column, max_score
    else:
        min_score = WIN_SCORE
        best_column = None
        for column in range(7):
            if is_valid_move(game_board, column):
                game_board = make_move(copy.deepcopy(game_board), copy.deepcopy(column), BLUE)
                _, score = alphabetapruning(copy.deepcopy(board), depth - 1, alpha, beta, True)
                if score < min_score:
                    min_score = score
                    best_column = copy.deepcopy(column)
                beta = min(beta, min_score)
                if beta <= alpha:
                    break
        return best_column, min_score



    # Check columns
    for i in range(3):
        for j in range(7):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                if board[i][j] == RED:
                    return WIN_SCORE
                elif board[i][j] == BLUE:
                    return -WIN_SCORE

# Check diagonal (left to right)
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                if board[i][j] == RED:
                    return WIN_SCORE
                elif board[i][j] == BLUE:
                    return -WIN_SCORE
