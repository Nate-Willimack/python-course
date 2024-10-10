import chess
import chess.engine
import chess.pgn

# Function to display the board
def print_board(board):
    print(board)

# Function to play a move
def play_move(board, move):
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move. Please try again.")

def main():
    board = chess.Board()
    
    while not board.is_game_over():
        print_board(board)
        if board.turn == chess.WHITE:
            print("White's turn.")
        else:
            print("Black's turn.")
        
        # Get user input for the move
        move = input("Enter your move (in standard algebraic notation, e.g., e2e4 or Nf3): ")
        
        # Play the move
        play_move(board, move)
        
        # Check if the game is over
        if board.is_checkmate():
            print("Checkmate!")
            break
        elif board.is_stalemate():
            print("Stalemate!")
            break
        elif board.is_insufficient_material():
            print("Draw due to insufficient material!")
            break
        elif board.is_seventyfive_moves():
            print("Draw due to the 75-move rule!")
            break
        elif board.is_fivefold_repetition():
            print("Draw due to fivefold repetition!")
            break

    # Print final board
    print_board(board)
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            print("White wins!")
        else:
            print("Black wins!")
    else:
        print("Game over with a draw.")

if __name__ == "__main__":
    main()
