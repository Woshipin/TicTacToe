class TicTacToe:
    
    def __init__(self, starting_player='X'):
        # Initialize the board, each position is an empty space
        self.board = {i: ' ' for i in range(1, 10)}
        # Set the current player based on the choice
        self.current_player = starting_player

    def print_board(self, show_positions=False):
        board = self.board
        if show_positions:
            # Print the positions for the first time
            print("1 | 2 | 3")
            print("--+---+--")
            print("4 | 5 | 6")
            print("--+---+--")
            print("7 | 8 | 9")
            print("----------\n")
        else:
            # Print the current state of the board
            print(f"{board[1]} | {board[2]} | {board[3]}")
            print("--+---+--")
            print(f"{board[4]} | {board[5]} | {board[6]}")
            print("--+---+--")
            print(f"{board[7]} | {board[8]} | {board[9]}")

    def check_winner(self, mark):
        # Define winning conditions
        win_conditions = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]
        # Check if any winning condition is met
        for condition in win_conditions:
            if all(self.board[pos] == mark for pos in condition):
                return True
        return False

    def is_board_full(self):
        # Check if the board is full
        return all(value != ' ' for value in self.board.values())

    def make_move(self, position):
        # Attempt to make a move at the specified position
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        # Switch the current player
        self.current_player = 'O' if self.current_player == 'X' else 'X'