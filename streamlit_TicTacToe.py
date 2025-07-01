import os

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.move_history = []

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        for i in range(3):
            row = " | ".join(self.board[i*3:(i+1)*3])
            print(" " + row)
            if i < 2:
                print("---+---+---")
        print("\n")

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.move_history.append(position)
            return True
        return False

    def undo_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            self.board[last_move] = ' '
            self.switch_player()
            print("Last move undone.")
        else:
            print("No move to undo.")

    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != ' ':
                return self.board[pattern[0]]
        return None

    def is_draw(self):
        return ' ' not in self.board

    def restart_game(self):
        self.__init__()

    def start(self):
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn (1-9), u for undo, r to restart:")
            user_input = input("Enter your move: ").strip().lower()

            if user_input == 'u':
                self.undo_move()
                continue
            elif user_input == 'r':
                self.restart_game()
                continue
            elif user_input in [str(i) for i in range(1, 10)]:
                pos = int(user_input) - 1
                if self.make_move(pos):
                    winner = self.check_winner()
                    if winner:
                        self.display_board()
                        print(f"🎉 Player {winner} wins!")
                        if input("Play again? (y/n): ").strip().lower() == 'y':
                            self.restart_game()
                        else:
                            break
                    elif self.is_draw():
                        self.display_board()
                        print("It's a draw!")
                        if input("Play again? (y/n): ").strip().lower() == 'y':
                            self.restart_game()
                        else:
                            break
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. Cell already taken.")
            else:
                print("Invalid input. Enter 1-9, 'u' to undo, or 'r' to restart.")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.start()
