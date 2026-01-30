import tkinter as tk
import math

root = tk.Tk()
root.title("Unbeatable Tic Tac Toe")
root.resizable(False, False)

board = [' ' for _ in range(9)]
buttons = []

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for win in wins:
        if all(board[i] == player for i in win):
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

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
    buttons[move].config(text='O', state='disabled')

def on_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X', state='disabled')

        if check_winner('X'):
            end_game("You win")
            return
        if is_draw():
            end_game("Draw")
            return

        ai_move()

        if check_winner('O'):
            end_game("AI wins")
        elif is_draw():
            end_game("Draw")

def end_game(msg):
    for b in buttons:
        b.config(state='disabled')
    label.config(text=msg)

for i in range(9):
    btn = tk.Button(
        root,
        text=' ',
        font=('Arial', 24),
        width=5,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

label = tk.Label(root, text="You are X | AI is O", font=('Arial', 12))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
