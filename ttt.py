"""
Author: Alex Black
Purpose: Allows two players to play a game of Tic-Tac-Toe against each other.
"""

def initialize_board():
    """Creates tic-tac-toe board."""
    board = [[" " for d in range(3)] for d in range(3)]
    return board

def display_board(board):
    """Prints the updated game board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board):
    """Checks if there is a winner."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player, board):
    """Gets the player's move."""
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def switch_player(current_player):
    """Switches the turn between players."""
    return "O" if current_player == "X" else "X"

def main():
    """Main function to connect all the pieces together to get program to fully run."""
    board = initialize_board()
    current_player = "X"
    while True:
        display_board(board)
        get_player_move(current_player, board)
        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            break
        current_player = switch_player(current_player)

main()

"""Design Document

Main Function

Purpose: It takes all the other functions that were created into one bigger function. Description: Contains the main loop, player turns, and checks for game over.

initialize_board()

Purpose: Creates the tic-tac-toe board.
Description: Creates a 3x3 board with empty spaces.

display_board(board)
Purpose: Prints the updated game board.
Description: Prints the board to the console for players to read.

check_win(board)
Purpose: Checks if there is a winner.
Description: Returns True if a player has won, otherwise False.

check_draw(board)
Purpose: Checks if the game is a draw.
Description: Returns True if the board is full and there is no winner.

get_player_move(player, board)
Purpose: Gets the current players move.
Description: Prompts the player for their move and updates the board.

switch_player(current_player)
Purpose: Switches the turn.
Description: Alternates between X and O.
"""
