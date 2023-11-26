THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20,pady=20, bg=THEME_COLOR)



        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.canvas.config(bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)
        self.question_text = self.canvas.create_text(150,125 ,text="Question", font=("Arial",20,"italic") , width=260)



        image_true = PhotoImage(file="images/true.png")
        image_false = PhotoImage(file="images/false.png")

        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_answer)
        self.button_true.grid(column=0,row=2, columnspan=1)
        self.button_false = Button(image=image_false, highlightthickness=0 ,command=self.false_answer)
        self.button_false.grid(column=1, row=2, columnspan=1)

        self.get_next_question()


        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Sccore: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the game")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)




    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)



    def give_feedback(self,is_right):

        if is_right == True:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")


        self.window.after(1000, self.get_next_question)


