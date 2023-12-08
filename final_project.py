import tkinter as tk
from tkinter import messagebox
import json

class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.text)
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")

    def validate_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

class MultipleChoiceQuestion(Question):
    def __init__(self, text, choices, correct_answer):
        super().__init__(text, choices, correct_answer)

class TrueFalseQuestion(Question):
    def __init__(self, text, correct_answer):
        super().__init__(text, ["True", "False"], correct_answer)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def get_next_question(self):
        return self.questions[self.current_question_index]

    def check_answer(self, user_answer):
        current_question = self.get_next_question()
        if current_question.validate_answer(user_answer):
            self.score += 1
            print("You are Correct! You get 1 point\n")
        else:
            print("You are Wrong :(\n")
        self.current_question_index += 1

    def has_questions_left(self):
        return self.current_question_index < len(self.questions)
    
    def is_quiz_over(self):
        return self.current_question_index >= len(self.questions)

def load_questions_from_file(filename, category):
    with open(filename, 'r') as file:
        data = json.load(file)
        questions = []
        for q in data['questions']:
            if q['category'] == category:
                if q['type'] == 'multiple_choice':
                    questions.append(MultipleChoiceQuestion(q['text'], q['choices'], q['answer']))
                elif q['type'] == 'true_false':
                    questions.append(TrueFalseQuestion(q['text'], q['answer']))
        return questions

class QuizGUI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Climate Change or Time to Change: The Quiz Game")
        
        self.question_label = tk.Label(self.window, text="", font=("Helvetica", 30))
        self.question_label.pack(pady=20)
        
        self.feedback_label = tk.Label(self.window, text="", font=("Helvetica", 20))
        self.feedback_label.pack(pady=20)

        self.answer_frame = tk.Frame(self.window)
        self.answer_frame.pack(pady=20)
        
        self.confirm_button = tk.Button(self.window, text="Confirm", command=self.check_answer)
        self.confirm_button.pack(pady=20)
        
        self.update_question()

    def update_question(self):
        if self.quiz.is_quiz_over():
            messagebox.showinfo("You Finished the Quiz, Congrats!", f"Good Job! Final score: {self.quiz.score}")
            self.window.destroy()
            return

        current_question = self.quiz.get_next_question()
        self.question_label.config(text=current_question.text)
        
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        for option in current_question.choices:
            btn = tk.Button(self.answer_frame, text=option, command=lambda opt=option: self.select_answer(opt))
            btn.pack(side=tk.LEFT, expand=True)

    def select_answer(self, answer):
        self.selected_answer = answer

    def clear_feedback(self):
        self.feedback_label.config(text="")

    def check_answer(self):
        correct = self.quiz.check_answer(self.selected_answer)
        if correct:
            self.feedback_label.config(text="Correct!", fg="green")
            self.quiz.score += 1
        else:
            self.feedback_label.config(text="Wrong!", fg="red")

        self.window.after(1000, self.clear_feedback)

        if self.quiz.is_quiz_over():
            messagebox.showinfo("Quiz Finished", f"Your final score is: {self.quiz.score}")
            self.window.destroy()
        else:
            self.window.after(1500, self.update_question)

    def run(self):
        self.window.mainloop()

def select_category():
    def start_quiz(category):
        questions = load_questions_from_file('final_project_2140/quiz_questions.json', category)
        quiz = Quiz(questions)
        app = QuizGUI(quiz)
        app.run()

    category_window = tk.Tk()
    category_window.title("Select Category")

    tk.Button(category_window, text="Easy", font=("Helvetica", 20), command=lambda: start_quiz("easy")).pack()
    tk.Button(category_window, text="Hard", font=("Helvetica", 20), command=lambda: start_quiz("hard")).pack()

    category_window.mainloop()

select_category()