import math

# Board setup
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    print(f"AI Bot has made its move at position {move + 1} 🌟")

# Main game loop
def play_game():
    print("Welcome, Aakarshi 🌸! Ready to challenge the AI Bot in Tic-Tac-Toe?")
    print("You are 'X' and AI Bot is 'O'. Let's begin!")
    print_board()

    while True:
        # Aakarshi's turn
        try:
            move = int(input("Your turn, Aakarshi! Choose a position (1-9): ")) - 1
            if board[move] != ' ' or move < 0 or move > 8:
                print("Oops! Invalid move. Try again.")
                continue
            board[move] = 'X'
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        print_board()

        if check_winner('X'):
            print("✨ Aakarshi wins! The universe smiles upon your strategy. ✨")
            break
        elif is_draw():
            print("It's a draw! A graceful balance between minds. 🤝")
            break

        # AI Bot's turn
        ai_move()
        print_board()

        if check_winner('O'):
            print("AI Bot wins! But don't worry, even stars stumble before they shine. 🌠")
            break
        elif is_draw():
            print("It's a draw! A graceful balance between minds. 🤝")
            break

# Start the game
play_game()
