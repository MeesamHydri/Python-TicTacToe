board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

def print_board(board):
    for n in range(len(board)):
        print(" | ".join(board[n]))
        if n < 2:
            print("-----------")

def make_move(board, row, col, symbol):
    if board[row][col] == " ":
        board[row][col] = symbol
        return True
    else:
        print("That spot is already taken! Try again.")
        return False

def get_valid_move(board, symbol):
    while True:
        try:
            row = int(input("Row (0-2): "))
            col = int(input("Col (0-2): "))

            if 0 <= row < len(board) and 0 <= col < len(board):
                if make_move(board, row, col, symbol):
                    return  # move placed successfully
            else:
                print("Invalid position! Please choose numbers 0, 1, or 2.")
        except ValueError:
            print("Please enter a number, not text!")

def check_winner(board, symbol):

    #check all rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # check all columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    #check all diagonals

    #Top left to bottom right
    if all(board[i][i] == symbol for i in range(3)):
        return True

    #Top right to bottom left
    if all(board[i][2-i] == symbol for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)


player_1 = input("Enter player 1 name: ")
player_2 = input("Enter player 2 name: ")

symbol_1 = "X"
symbol_2 = "O"

game_over = False

while not game_over:
    print_board(board)

    # Player 1 turn
    print(f"{player_1}'s turn ({symbol_1})")
    get_valid_move(board, symbol_1)
    print_board(board)
    if check_winner(board, symbol_1):
        print(f"{player_1} is the Winner! Congratulations")
        break
    if is_draw(board):
        print("It's a draw, No winner this time.")
        break

    # Player 2 turn
    print(f"{player_2}'s turn ({symbol_2})")
    get_valid_move(board, symbol_2)
    print_board(board)
    if check_winner(board, symbol_2):
        print(f"{player_2} is the Winner! Congratulations")
        break
    if is_draw(board):
        print("It's a draw, No winner this time.")
        break