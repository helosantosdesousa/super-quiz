import tkinter as tk
from model.quiz import Quiz

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Super Quiz')
    root.geometry('900x500')
    quiz = Quiz(root)
    root.mainloop()
