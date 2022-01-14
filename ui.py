from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Harry's Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     100,
                                                     width=280,
                                                     text="Question Text",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # create label
        self.score_label = Label(text="score: 0", font="Arial", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.score_label.config(padx=5, pady=5)


        # create button
        true_image = PhotoImage(file="/Users/harry/PycharmProjects/day34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="/Users/harry/PycharmProjects/day34/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have completed the quiz!")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





