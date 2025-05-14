from random import choice

# create empty board function
def create_board():
    """
    Create and returns an empty tic-tac-toe board
    """
    return [' '] * 9


# Display board function
def display_board(board):
    """
    Display the tic-tac-toe board
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# Player move input function
def get_player_move(board):
    """
    Gets the player move
    """
    while True:
        try:
            move = int(input("Choose a move (0-8): "))
            if (move >= 0) and (move <= 8) and (board[move] == ' '):
                return move
            else:
                print("Invalid move. Pls choose a number between 0 and 8, and choose an empty space")
        except ValueError:
            print("Invalid input. Please choose a  number between 0 and 8")


# AI move
def get_ai_move(board, player_marker='X', ai_marker='O'):
    """
    Gets the AI move using the following strategy
    1. Check for winning move
    2. Block player's winning move
    3. Choose a random empty space
    """

    def check_win_move(marker):
        """ Checks if there is a winning move for a given marker """
        for i in range(9):
            if board[i] == ' ': 
                temp_board = list(board) # creates a copy to avoid modifying the original board
                temp_board[i] = marker
                if check_win(temp_board, marker):
                    return i
        return None
    
    # check for AI winning move
    winning_move = check_win_move(ai_marker)
    if winning_move is not None:
        return winning_move
    
    # Block player winning move
    blocking_move = check_win_move(player_marker)
    if blocking_move is not None:
        return blocking_move
    
    # Choose a random empty space
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return choice(available_moves)

# check win function
def check_win(board, player):
    """
    Checks if the given player has won the game
    """
    # Check rows, columns, and diagonals
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2 ,4, 6]             # Diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return True 
    return False

# check tie function
def check_tie(board):
    """
    Checks if the game is a tie
    """
    return ' ' not in board

# Main game function
def play_game():
    """
    Main tic-tac-toe function
    """
    board = create_board()
    player_marker = 'X'
    ai_marker = 'O'
    current_player = player_marker # Start with the player

    print("This is a Tic-Tac-Toe game!")
    display_board(board)

    while True:
        if current_player == player_marker:
            move = get_player_move(board)
        else:
            move = get_ai_move(board, player_marker, ai_marker)

        board[move] = current_player
        display_board(board)

        if check_win(board, current_player):
            if current_player == player_marker:
                print("You Win!")
            else:
                print("AI Wins")
            break
        elif check_tie(board):
            print("It's a Tie")
            break

        # Switch players
        if current_player == player_marker:
            current_player = ai_marker
        else:
            current_player = player_marker


if __name__ == "__main__":
    play_game()
