from board import Board
import time
import alphabeta
import minimax


# Game constants
def main():
    alpha = alphabeta
    mini = minimax
    board = Board()
    time.sleep(2)
    game_end = False
    choice = int(input("please enter the heuristic style you want to use"))
    depthchoice = int(input("please enter the depth level you want to use"))
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        # Make the move
        if choice == 1:
            column, score = alpha.alphabetapruning(board, depth=depthchoice, alpha=-1000000000, beta=1000000000, maximizingPlayer=True)
            if column is not None:
                board.select_column(int(column))

        if choice == 2:
            column, score = mini.minimax(board, depth=depthchoice, maximizingPlayer=True)
            if column is not None:
                board.select_column(int(column))
        time.sleep(2)

if __name__ == "__main__":
    main()
