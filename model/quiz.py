import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
import requests
from model.question import Question


class Quiz:
    def __init__(self, window):
        self.window = window
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.right_answer = tk.IntVar()

        self.bg_color = '#ECECEC'
        self.text_color = '#333333'
        self.bt_color = '#4CAF50'
        self.bt_text_color = '#FFFFFF'

        self.window.config(bg=self.bg_color)
        self.window.option_add('*Font', 'Arial')

        # icon
        try:
            self.app_icon = PhotoImage(file='logo.png')
            self.app_label = tk.Label(window, image=self.app_icon, bg=self.bg_color)
            self.app_label.pack(pady=10)
        except:
            pass  

        # question label
        self.questions_label = tk.Label(
            window, text='', wraplength=380, bg=self.bg_color,
            fg=self.text_color, font=('Arial', 12, 'bold')
        )
        self.questions_label.pack(pady=20)

        # buttons
        self.op1_btn = tk.Button(window, width=30, bg=self.bt_color, fg=self.bt_text_color,
                                 font=('Arial', 10, 'bold'), command=lambda: self.check_answer(1))
        self.op2_btn = tk.Button(window, width=30, bg=self.bt_color, fg=self.bt_text_color,
                                 font=('Arial', 10, 'bold'), command=lambda: self.check_answer(2))
        self.op3_btn = tk.Button(window, width=30, bg=self.bt_color, fg=self.bt_text_color,
                                 font=('Arial', 10, 'bold'), command=lambda: self.check_answer(3))
        self.op4_btn = tk.Button(window, width=30, bg=self.bt_color, fg=self.bt_text_color,
                                 font=('Arial', 10, 'bold'), command=lambda: self.check_answer(4))

        self.op1_btn.pack(pady=10)
        self.op2_btn.pack(pady=10)
        self.op3_btn.pack(pady=10)
        self.op4_btn.pack(pady=10)

        # button play again
        self.play_again_btn = tk.Button(
            window, command=self.play_again, text='Play again', width=30,
            bg=self.bt_color, fg=self.bt_text_color, font=('Arial', 10, 'bold')
        )

       
        self.fetch_questions()
        self.display_question()

    def fetch_questions(self):
        url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                question_text = item['question']
                correct_answer = item['correct_answer']
                options = item['incorrect_answers'] + [correct_answer]
                random.shuffle(options)
                question = Question(question_text, options, correct_answer)
                self.questions.append(question)
        else:
            messagebox.showerror("Error", "Failed to fetch questions.")
            self.window.quit()

    def display_question(self):
        question = self.questions[self.current_question]
        self.questions_label.config(text=question.question_text)

        self.op1_btn.config(text=question.options[0], state=tk.NORMAL)
        self.op2_btn.config(text=question.options[1], state=tk.NORMAL)
        self.op3_btn.config(text=question.options[2], state=tk.NORMAL)
        self.op4_btn.config(text=question.options[3], state=tk.NORMAL)

        self.right_answer.set(question.options.index(question.right_answer) + 1)

    def check_answer(self, selected_option):
        if selected_option == self.right_answer.get():
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo('Quiz completed', f'Congratulations You finished the Super Quiz!\nScore: {self.score}/{len(self.questions)}')
        self.disable_buttons()
        self.play_again_btn.pack()

    def play_again(self):
        self.score = 0
        self.current_question = 0
        random.shuffle(self.questions)
        self.enable_buttons()
        self.play_again_btn.pack_forget()
        self.display_question()

    def disable_buttons(self):
        self.op1_btn.config(state=tk.DISABLED)
        self.op2_btn.config(state=tk.DISABLED)
        self.op3_btn.config(state=tk.DISABLED)
        self.op4_btn.config(state=tk.DISABLED)

    def enable_buttons(self):
        self.op1_btn.config(state=tk.NORMAL)
        self.op2_btn.config(state=tk.NORMAL)
        self.op3_btn.config(state=tk.NORMAL)
        self.op4_btn.config(state=tk.NORMAL)
