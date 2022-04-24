from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title('Quizzler')

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   width=200,
                                                   text='a',
                                                   font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        self.lbl_score = Label(text='Score: ', bg=THEME_COLOR, fg='white')
        self.lbl_score.grid(row=0, column=1)

        self.true_img = PhotoImage(file='./images/true.png')
        self.btn_true = Button(image=self.true_img, command=self.true_button_pressed)
        self.btn_true.grid(row=2, column=0)

        self.false_img = PhotoImage(file='./images/false.png')
        self.btn_false = Button(image=self.false_img, command=self.false_button_pressed)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.btn_true.config(state='normal')
        self.btn_false.config(state='normal')
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.lbl_score.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text='You have reached the end of the quiz')
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')

    def true_button_pressed(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_button_pressed(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')
        else:
            self.canvas.config(bg='red')
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')
        self.window.after(1000, self.get_next_question)
