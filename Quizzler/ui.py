from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizApp:
    
    def __init__(self, quizbrain):
        
        self.quiz = quizbrain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font= ("Arial", 10, "bold"))
        self.score_text.grid(row=0, column=2, pady=20)
        
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial",20,"italic"), fill="black")
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check)
        
        self.true_button.grid(row=2, column=1, pady=20)
        
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_check)
        
        self.false_button.grid(row=2, column=2, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_check(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
            
    def false_check(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            
        self.window.after(500, self.get_next_question)