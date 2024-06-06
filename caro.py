import tkinter as tk
import numpy as np

# Initialize the game board
def init_board():
    return np.zeros((3, 3), dtype=int)

# Check for a win
def check_win(board):
    for i in range(3):
        if abs(sum(board[i, :])) == 3 or abs(sum(board[:, i])) == 3:
            return True
    if abs(board[0, 0] + board[1, 1] + board[2, 2]) == 3 or abs(board[0, 2] + board[1, 1] + board[2, 0]) == 3:
        return True
    return False

# Check for a full board (draw)
def check_full(board):
    return not (board == 0).any()

# AI move (simple strategy)
def ai_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
                board[i, j] = player
                return

# Handle a button click
def button_click(row, col):
    global current_player
    if board[row, col] == 0:
        board[row, col] = current_player
        buttons[row][col].config(text='X' if current_player == 1 else 'O', state='disabled')
        
        if check_win(board):
            result_label.config(text=f"Player {'X' if current_player == 1 else 'O'} wins!")
            disable_all_buttons()
            return
        if check_full(board):
            result_label.config(text="It's a draw!")
            return
        
        current_player *= -1
        
        if current_player == -1:
            ai_move(board, current_player)
            update_buttons()
            if check_win(board):
                result_label.config(text="Player O wins!")
                disable_all_buttons()
                return
            if check_full(board):
                result_label.config(text="It's a draw!")
                return
            current_player *= -1

def update_buttons():
    for i in range(3):
        for j in range(3):
            if board[i, j] == 1:
                buttons[i][j].config(text='X', state='disabled')
            elif board[i, j] == -1:
                buttons[i][j].config(text='O', state='disabled')

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = init_board()
current_player = 1  # 1 for 'X', -1 for 'O'

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text='', width=10, height=3, command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
