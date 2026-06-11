import math

# ─────────────────────────────────────────
#  BOARD SETUP
# ─────────────────────────────────────────
def create_board():
    return [' '] * 9

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f"  {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("  --|---|--")
    print("\n  1   2   3")
    print("  4   5   6")
    print("  7   8   9\n")

# ─────────────────────────────────────────
#  GAME LOGIC
# ─────────────────────────────────────────
WIN_COMBOS = [
    [0,1,2],[3,4,5],[6,7,8],  # rows
    [0,3,6],[1,4,7],[2,5,8],  # cols
    [0,4,8],[2,4,6]           # diagonals
]

def check_winner(board):
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    if ' ' not in board:
        return 'draw'
    return None

def get_empty_cells(board):
    return [i for i, v in enumerate(board) if v == ' ']

# ─────────────────────────────────────────
#  MINIMAX WITH ALPHA-BETA PRUNING
# ─────────────────────────────────────────
def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result == 'O':     return 10 - depth
    if result == 'X':     return depth - 10
    if result == 'draw':  return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty_cells(board):
            board[i] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i] = ' '
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in get_empty_cells(board):
            board[i] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = ' '
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def get_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in get_empty_cells(board):
        board[i] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = ' '
        if score > best_score:
            best_score = score
            best_move = i
    return best_move

# ─────────────────────────────────────────
#  HUMAN MOVE
# ─────────────────────────────────────────
def human_move(board):
    while True:
        try:
            move = int(input("  Your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("  Enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("  That cell is already taken! Try again.")
            else:
                return move
        except ValueError:
            print("  Invalid input. Enter a number 1-9.")

# ─────────────────────────────────────────
#  MAIN GAME LOOP
# ─────────────────────────────────────────
def play_game():
    print("\n" + "="*40)
    print("   TIC-TAC-TOE AI  |  CodSoft Task 2")
    print("   Minimax + Alpha-Beta Pruning")
    print("="*40)
    print("\n  You = X    AI = O\n")

    scores = {'X': 0, 'O': 0, 'Draw': 0}

    while True:
        board = create_board()
        current = 'X'

        while True:
            print_board(board)

            if current == 'X':
                print("  >> Your turn (X)")
                move = human_move(board)
                board[move] = 'X'
            else:
                print("  >> AI is thinking...")
                move = get_best_move(board)
                board[move] = 'O'
                print(f"  AI played position {move + 1}")

            result = check_winner(board)

            if result:
                print_board(board)
                if result == 'X':
                    print("  *** You win! Congratulations! ***\n")
                    scores['X'] += 1
                elif result == 'O':
                    print("  *** AI wins! Better luck next time. ***\n")
                    scores['O'] += 1
                else:
                    print("  *** It's a draw! ***\n")
                    scores['Draw'] += 1

                print(f"  Score  ->  You: {scores['X']}  |  AI: {scores['O']}  |  Draw: {scores['Draw']}")
                break

            current = 'O' if current == 'X' else 'X'

        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Thanks for playing! Goodbye!\n")
            break

# ─────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────
if __name__ == "__main__":
    play_game()
