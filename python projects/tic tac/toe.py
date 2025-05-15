def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    if all(board[i][i] == player for i in range(3)):  # Diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_game():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        move = int(move)
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()

# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
#     print("\n")

# def check_winner(board, player):
#     # Check rows, columns and diagonals
#     for i in range(3):
#         if all(cell == player for cell in board[i]):  # Row
#             return True
#         if all(board[j][i] == player for j in range(3)):  # Column
#             return True
#     if all(board[i][i] == player for i in range(3)):  # Diagonal
#         return True
#     if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
#         return True
#     return False

# def is_full(board):
#     return all(cell in ['X', 'O'] for row in board for cell in row)

# def play_game():
#     board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#     current_player = "X"

#     print("Welcome to Tic-Tac-Toe!\n")
#     print_board(board)

#     while True:
#         move = input(f"Player {current_player}, enter your move (1-9): ")

#         if not move.isdigit() or not (1 <= int(move) <= 9):
#             print("Invalid input. Please enter a number between 1 and 9.")
#             continue

#         move = int(move)
#         row = (move - 1) // 3
#         col = (move - 1) % 3

#         if board[row][col] in ['X', 'O']:
#             print("That spot is already taken. Try again.")
#             continue

#         board[row][col] = current_player
#         print_board(board)

#         if check_winner(board, current_player):
#             print(f"🎉 Player {current_player} wins!")
#             break

#         if is_full(board):
#             print("It's a draw!")
#             break

#         # Switch player
#         current_player = "O" if current_player == "X" else "X"

# # Run the game
# if _name_ == "_main_":
#     play_game()

# # Function to print the Tic-Tac-Toe board
# def print_board(board):
#     print("\n")  # Print a newline for formatting
#     for row in board:  # Iterate over each row in the board
#         print(" | ".join(row))  # Join the elements of the row with | for better display
#         print("-" * 9)  # Print a line separator
#     print("\n")  # Print a newline for formatting

# # Function to check if a player has won
# def check_winner(board, player):
#     # Check rows, columns, and diagonals for a win
#     for i in range(3):
#         if all(cell == player for cell in board[i]):  # Check if all cells in the row are equal to player
#             return True  # Player wins if this condition is met
#         if all(board[j][i] == player for j in range(3)):  # Check if all cells in the column are equal to player
#             return True  # Player wins if this condition is met
    
#     # Check diagonals for a win
#     if all(board[i][i] == player for i in range(3)):  # Check the main diagonal
#         return True  # Player wins if this condition is met
#     if all(board[i][2 - i] == player for i in range(3)):  # Check the anti-diagonal
#         return True  # Player wins if this condition is met
    
#     return False  # Return False if no winner found

# # Function to check if the board is full (no empty spaces left)
# def is_full(board):
#     return all(cell in ['X', 'O'] for row in board for cell in row)  # Check if all cells are occupied by X or O

# # Main function to control the game flow
# def play_game():
#     # Initialize the board with numbers 1-9
#     board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#     current_player = "X"  # Start with player X

#     print("Welcome to Tic-Tac-Toe!\n")  # Print welcome message
#     print_board(board)  # Print the initial board

#     while True:  # Loop until there is a winner or the board is full
#         # Ask the current player for their move
#         move = input(f"Player {current_player}, enter your move (1-9): ")

#         # Check if the input is a valid number between 1 and 9
#         if not move.isdigit() or not (1 <= int(move) <= 9):
#             print("Invalid input. Please enter a number between 1 and 9.")  # Invalid input message
#             continue  # Ask the player again

#         move = int(move)  # Convert the input to an integer
#         row = (move - 1) // 3  # Calculate the row based on the move
#         col = (move - 1) % 3  # Calculate the column based on the move

#         # Check if the selected spot is already occupied
#         if board[row][col] in ['X', 'O']:
#             print("That spot is already taken. Try again.")  # Occupied spot message
#             continue  # Ask the player to try again

#         board[row][col] = current_player  # Mark the spot with the current player's symbol
#         print_board(board)  # Print the updated board

#         # Check if the current player has won
#         if check_winner(board, current_player):
#             print(f"🎉 Player {current_player} wins!")  # Victory message
#             break  # End the game

#         # Check if the board is full and it's a draw
#         if is_full(board):
#             print("It's a draw!")  # Draw message
#             break  # End the game

#         # Switch the player for the next turn
#         current_player = "O" if current_player == "X" else "X"  # Switch player

# # Run the game if this script is being executed as the main program
# if __name__ == "__main__":
#     play_game()  # Call the function to start the game
