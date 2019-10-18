import tkinter as tk
from tkinter import font as fn



# font

# fon = fn.Font(family='Great Vibes', size=16, weight='bold') text='Welcome to the game, please what is your name'

game_win = tk.Tk()
game_win.title('Text Adventure game')
game_win.geometry('1000x1000')
can = tk.Canvas(game_win, height=1900, width=900)
can.pack()

# the following are done when creating the frame for my game
# relheight and relwidth are same as height and width but there number is from 0 - 1
# relx and rely are the offset of the vertical and horizontal but there number is from 0 - 1

# upper frame
up_fra = tk.Frame(game_win, bg='#00ffff', bd=5)
up_fra.place(relheight=0.1, relwidth=0.6, relx=0.5, rely=0.01, anchor='n')

# design frame
low_frame = tk.Frame(game_win, bg='#00ffff', bd=5)
low_frame.place(relheight=0.8, relwidth=0.5, relx=0.5, rely=0.15, anchor='n')

#  frame of name of game
# name_frame = tk.Frame(game_win, bg='pink')
# name_frame.place(relheight=0.14, relwidth=0.55, relx=0.23, rely=0.01)


# question frame
question_frame = tk.Frame(low_frame, bg='white')
question_frame.place(relheight=0.5, relwidth=0.99, relx=0.004, rely=0.01, anchor='nw')

# answer frame
ans_frame = tk.Frame(low_frame, bg='#3bb9ff')
ans_frame.place(relheight=0.1, relwidth=0.92, relx=0.5, rely=0.53, anchor='n')

# button frame
# but_frame = tk.Frame(game_win, bg='yellow')
# but_frame.place(relheight=0.1, relwidth=0.6, rely=0.76, relx=0.2)


# game name and user name label inside our frame
name_label = tk.Label(up_fra, text='ZORO AND THE BLIND WINCH', bg='#00ffff', fg='#ff00ff', font=('Algerian', 30, 'bold'))
name_label.place(relheight=0.4, relwidth=0.99, relx=0, rely=0.3)

# name_label = tk.Label(name_frame, text='yello', bg='yellow', font=('copper black', 14, 'bold'))
# name_label.place(relheight=0.3, relwidth=0.99, relx=0, rely=0.8)

# question label
qes_var = tk.StringVar()
question_label = tk.Message(question_frame, text='''hvdvdvto tvvdvdvdhe worvvfvfvdld''', bg='white', font=('copper black', 26, 'bold'), fg='#ff00ff')
question_label.place(relheight=0.8, relwidth=0.97, y=26, x=10)


# answer entry and button

ans_entry = tk.Entry(ans_frame, font=('copper black', 20, 'bold'))
ans_entry.place(relheight=0.79, relwidth=0.59, relx=0.02, rely=0.1)

next_button = tk.Button(ans_frame, bg='#ebf5fb', text='NEXT_MOVE', fg='#00ffff', font=('copper black', 16, 'bold'))
next_button.place(relheight=0.79, relwidth=0.3, relx=0.64, rely=0.1)


# button for next and reset
reset_button = tk.Button(low_frame, bg='#ff00ff', text='RESET', fg='white', font=('copper black', 16, 'bold'))
reset_button.place(relheight=0.15, relwidth=0.26, relx=0.5, rely=0.64, anchor='n')





game_win.mainloop()