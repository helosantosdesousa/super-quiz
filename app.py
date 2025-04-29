import tkinter as tk 
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

print(questions)

window=tk.Tk()
window.title('Quiz')
window.geometry('400x450')

bg_color = '#ECECEC'
text_color = '#333333'
bt_color = '#4CAF50'
bt_text_color = '#FFFFFF'

window.config(bg=bg_color)
window.option_add('*Font', 'Arial')

# icon
app_icon = PhotoImage(file='logo.png')
app_label = tk.Label(window, image=app_icon,bg=bg_color)
app_label.pack(pady=10)

# ui componets
questions_label = tk.Label(window, text='Question', wraplength=380, bg=bg_color, fg=text_color, font=('Arial',12,'bold'))
questions_label.pack(pady=20)

right_answer = tk.IntVar()
op1_btn = tk.Button(window, text='', width=30, bg=bt_color, fg=bt_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
op1_btn.pack(pady=10)

op2_btn = tk.Button(window, text='', width=30, bg=bt_color, fg=bt_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
op2_btn.pack(pady=10)

op3_btn = tk.Button(window, text='', width=30, bg=bt_color, fg=bt_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
op3_btn.pack(pady=10)

op4_btn = tk.Button(window, text='', width=30, bg=bt_color, fg=bt_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
op4_btn.pack(pady=10)


play_again_btn = tk.Button(window, text='Play again', width=30, bg=bt_color, fg=bt_text_color, font=('Arial', 10, 'bold'))
play_again_btn.pack(pady=10)

window.mainloop()