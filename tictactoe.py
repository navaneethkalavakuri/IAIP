# Tic Tac Toe Game in Python

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

            # Validate input
            if row not in range(3) or col not in range(3):
                print("Invalid position! Please choose between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue

            # Place player mark
            board[row][col] = current_player

            # Check for winner
            if check_winner(board, current_player):
                display_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            # Check for tie
            if check_tie(board):
                display_board(board)
                print("🤝 It's a tie!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter valid numbers.")


# Main Program
while True:
    print("===== TIC TAC TOE =====")
    play_game()

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break