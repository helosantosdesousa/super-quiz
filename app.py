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
background_color = '#ECECEC'
text_color = '#333333'
bt_color = '#4CAF50'

window.config(bg=background_color)
window.option_add('*Font', 'Arial')

window.mainloop()