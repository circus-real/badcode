def display_board(board):
    """Displays the current state of the game board."""
    print("\n")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print("\n")
    print("\n")

def get_move(player):
    """Gets a valid move from the given player."""
    while True:
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move, try again.")
            continue
        if board[row][col] != "-":
            print("That space is already taken, try again.")
            continue
        return row, col

def check_win(board, player):
    """Checks if the given player has won the game."""
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# initialize the game board with empty cells
board = [["-" for _ in range(3)] for _ in range(3)]

# loop until the game is over
while True:
    # display the current state of the game board
    display_board(board)

    # get the next move from player 0
    row, col = get_move(0)
    board[row][col] = "0"

    # check if player 0 has won the game
    if check_win(board, "0"):
        print("Player 0 wins!")
        display_board(board)
        break

    # display the current state of the game board
    display_board(board)

    # get the next move from player X
    row, col = get_move("X")
    board[row][col] = "X"

    # check if player X has won the game
    if check_win(board, "X"):
        print("Player X wins!")
        display_board(board)
        break
