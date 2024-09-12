import random

def initialize_board(size):
    """Initialize the game board with pairs of numbers."""
    numbers = list(range(size * size // 2)) * 2
    random.shuffle(numbers)
    return [numbers[i:i+size] for i in range(0, len(numbers), size)]

def print_board(board, revealed):
    """Print the game board."""
    for i, row in enumerate(board):
        print(' '.join(str(cell) if revealed[i][j] else '*' for j, cell in enumerate(row)))

def get_coordinates():
    """Get valid coordinates from the player or handle exit command."""
    while True:
        try:
            user_input = input("Enter row and column (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                return None, None  # Signal to exit the game
            row, col = map(int, user_input.split())
            if row >= 0 and col >= 0:
                return row, col
            else:
                print("Row and column must be non-negative integers.")
        except ValueError:
            print("Invalid input. Please enter integers or type 'exit'.")

def play_memory_game(size):
    """Main function to play the memory game."""
    board = initialize_board(size)
    revealed = [[False] * size for _ in range(size)]
    matches_found = 0
    total_matches = (size * size) // 2
    attempts = 0

    while matches_found < total_matches:
        print_board(board, revealed)

        # Get first card
        print("Select the first card:")
        row1, col1 = get_coordinates()
        if row1 is None:  # User chose to exit
            print("Exiting the game. Goodbye!")
            return
        while revealed[row1][col1]:
            print("Card already revealed. Choose another card.")
            row1, col1 = get_coordinates()
            if row1 is None:  # User chose to exit
                print("Exiting the game. Goodbye!")
                return
        
        revealed[row1][col1] = True
        print_board(board, revealed)

        # Get second card
        print("Select the second card:")
        row2, col2 = get_coordinates()
        if row2 is None:  # User chose to exit
            print("Exiting the game. Goodbye!")
            return
        while (row2 == row1 and col2 == col1) or revealed[row2][col2]:
            print("Card already revealed or same card. Choose another card.")
            row2, col2 = get_coordinates()
            if row2 is None:  # User chose to exit
                print("Exiting the game. Goodbye!")
                return
        
        revealed[row2][col2] = True
        print_board(board, revealed)

        # Check if the cards match
        if board[row1][col1] == board[row2][col2]:
            print("Match found!")
            matches_found += 1
        else:
            print("No match. Try again.")
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        
        attempts += 1

    print(f"Congratulations! You've found all matches in {attempts} attempts.")

if __name__ == "__main__":
    size = 4  # Example size; should be even and >= 2
    play_memory_game(size)
