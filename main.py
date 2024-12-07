# Importing a random number generator function.
import random

# Greets, sets name, and variables.
print("Welcome to Tic-Tac-Toe.")
name = input("Enter Player Name = ")


def clear():
    print("\033[H\033[J", end="")


clear()
print("Hello", name + "!")
print("\n")

# Sets values for each grid, 0 is empty, Computer: 1, Player: 2.
board = {
    "tL": 0,
    "tM": 0,
    "tR": 0,
    "mL": 0,
    "mM": 0,
    "mR": 0,
    "bL": 0,
    "bM": 0,
    "bR": 0,
}

# Tracks who's making a move, Computer: 1, Player: 2, set to 1, Computer always starts.
current_player = 1

# Function to draw the board.
def draw_board():
    for row in ["t", "m", "b"]:
        for col in ["L", "M", "R"]:
            if board[row + col] == 0:
                print("   ", end="")
            elif board[row + col] == 1:
                print("\033[91m" + " X ", end="\033[0m")
            else:
                print("\033[96m" + " O ", end="\033[0m")
            if col != "R":
                print("|", end="")
        print()
        if row != "b":
            print("---+---+---")


# Function to check for a win.
def check_win():
    win_conditions = [
        ["tL", "tM", "tR"],
        ["mL", "mM", "mR"],
        ["bL", "bM", "bR"],  # Rows
        ["tL", "mL", "bL"],
        ["tM", "mM", "bM"],
        ["tR", "mR", "bR"],  # Columns
        ["tL", "mM", "bR"],
        ["tR", "mM", "bL"],  # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != 0:
            return board[condition[0]]
    return 0


# Function to play a move.
def play(spot):
    global current_player
    if board[spot] == 0:
        board[spot] = current_player
        current_player = 2 if current_player == 1 else 1
    else:
        print("Spot already taken. Try again.")


# Main game loop.
print("\nComputer will go first.")
draw_board()

while True:
    if current_player == 1:
        spot = random.choice([k for k, v in board.items() if v == 0])
        play(spot)
        print("\nComputer played at", spot)
    else:
        spot = input("Enter your move (tL, tM, tR, mL, mM, mR, bL, bM, bR): ")
        if spot in board:
            play(spot)
        else:
            print("Invalid move. Try again.")
            continue  # Skip the rest of the loop iteration and prompt again.

    clear()
    draw_board()

    winner = check_win()
    if winner != 0:
        if winner == 1:
            print("Computer wins!")
        else:
            print("Congratulations", name + ", you win!")
        break
    elif all(value != 0 for value in board.values()):
        print("It's a tie!")
        break
