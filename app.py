import tkinter as tk 
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random


#read excel questions
df = pd.read_excel('questions.xlsx')
# get questions ramdomly
questions = df.sample(n=10).values.tolist()

# global var
score = 0
current_question = 0

"""
    Displays the current question and enables the answer buttons.

    This function updates the `questions_label` with the current question text
    and sets the text and state of the answer buttons (`op1_btn`, `op2_btn`, 
    `op3_btn`, `op4_btn`) to allow user interaction.
"""


def display_question():
    question, op1, op2,op3,op4, answer = questions[current_question]
    questions_label.config(text=question)
    op1_btn.config(text=op1, state=tk.NORMAL, command=lambda:check_answer(1))
    op2_btn.config(text=op2, state=tk.NORMAL,command=lambda:check_answer(2))
    op3_btn.config(text=op3, state=tk.NORMAL,command=lambda:check_answer(3))
    op4_btn.config(text=op4, state=tk.NORMAL,command=lambda:check_answer(4))
    
    right_answer.set(answer)  
    

def show_result():
    messagebox.showinfo('Quiz completed', f'Congrats! You finished the quiz!\n Score: {score}/{len(questions)}')   
    op1_btn.config(state=tk.DISABLED)
    op2_btn.config(state=tk.DISABLED)
    op3_btn.config(state=tk.DISABLED) 
    op4_btn.config(state=tk.DISABLED)
    
    play_again_btn.pack()
    
    
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    
    op1_btn.config(state=tk.NORMAL)
    op2_btn.config(state=tk.NORMAL)
    op3_btn.config(state=tk.NORMAL)
    op4_btn.config(state=tk.NORMAL)
    
    play_again_btn.pack_forget()        

 

def check_answer(selected_op):
    global score, current_question
    
    if selected_op == right_answer.get():
        score+=1
        
    current_question+=1
    
    if current_question<len(questions):
        display_question()
    else:
        show_result()    

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
questions_label = tk.Label(window, text='', wraplength=380, bg=bg_color, fg=text_color, font=('Arial',12,'bold'))
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


play_again_btn = tk.Button(window, command=play_again, text='Play again', width=30, bg=bt_color, fg=bt_text_color, font=('Arial', 10, 'bold'))


display_question()
window.mainloop()