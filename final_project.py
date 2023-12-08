import tkinter as tk
from tkinter import messagebox
import json

class Question:
    def __init__(self, text, choices, correct_answer):
        """
        Initializes a new Question instance.
        
        - Parameters:
        text (str): The question text.
        choices (list): A list of answer choices.
        correct_answer (str): The correct answer.
        """
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def display_question(self):
        """Prints question and the choices to console."""

        print(self.text)
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")

    def validate_answer(self, user_answer):
        """
        Validates the user's answer with the correct answer.

        - Parameters:
        user_answer (str): The user's answer.

        - Returns:
        bool: True if the answer is correct, False otherwise.
        """
        return user_answer.lower() == self.correct_answer.lower()

class MultipleChoiceQuestion(Question): # inherits from Question class
    def __init__(self, text, choices, correct_answer):
        super().__init__(text, choices, correct_answer)

class TrueFalseQuestion(Question): # inherits from Question class
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
        """
        Checks the given answer with the current question's answer.

        - Parameters:
        user_answer (str): The user's answer.

        - Returns:
        A bool: True if answer is corect and False if not.
        """
        current_question = self.get_next_question()
        correct = current_question.validate_answer(user_answer)
        self.current_question_index += 1 

        if correct:
            self.score += 1
            print("You are Correct! You get 1 point\n")
            return True
        else:
            print("You are Wrong :(\n")
            return False

    def has_questions_left(self):
        return self.current_question_index < len(self.questions)
    
    def is_quiz_over(self):
        return self.current_question_index >= len(self.questions)

def load_questions_from_file(filename, category):
    """
    Loads the quiz's questions from the JSON file for a certain category, hard or eady.

    - Parameters:
    filename (str): Directory path to JSON file.
    category (str): Category of questions to load.

    - Returns:
    list: A list of Question objects.
    """
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

class QuizGUI: # This is the graphical user interface for the quiz application. 
    def __init__(self):
        """
        Initializes the main window and starts the game.
        """
        self.window = tk.Tk()
        self.window.title("Climate Change or Time to Change: The Quiz Game")
        self.start_screen()

    def start_screen(self):
        """
        Launches the start window with the title of the game and a start button.
        """
        self.start_frame = tk.Frame(self.window)
        self.start_frame.pack(pady=20)

        tk.Label(self.start_frame, text="Climate Change or Time to Change: The Quiz Game", font=("Helvetica", 40)).pack(pady=20)
        tk.Button(self.start_frame, text="Start Quiz", font=("Helvetica", 30), command=self.category_selection).pack()

    def category_selection(self):
        """
        Displays the wimdow with two categories to choose from.
        """
        self.start_frame.destroy()

        self.category_frame = tk.Frame(self.window)
        self.category_frame.pack(pady=20)

        tk.Label(self.category_frame, text="Select a Category:", font=("Helvetica", 40)).pack(pady=20)
        tk.Button(self.category_frame, text="Easy Mode", font=("Helvetica", 20), command=lambda: self.start_quiz("easy")).pack()
        tk.Button(self.category_frame, text="Hard Mode", font=("Helvetica", 20), command=lambda: self.start_quiz("hard")).pack()

    def start_quiz(self, category):
        self.category_frame.destroy()

        self.quiz = Quiz(load_questions_from_file('final_project_2140/quiz_questions.json', category))
        self.setup_quiz_interface()

    def setup_quiz_interface(self):
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
        correct = self.quiz.check_answer(self.selected_answer.lower())
        if correct:
            self.feedback_label.config(text="Correct! You get 1 point!", fg="green")
        else:
            self.feedback_label.config(text="Wrong :(", fg="red")

        self.window.after(1000, self.clear_feedback)

        if self.quiz.is_quiz_over():
            messagebox.showinfo("Quiz Finished", f"Quiz Finished! Congrats your final score is: {self.quiz.score}")
            self.window.destroy()
        else:
            self.window.after(1700, self.update_question)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = QuizGUI()
    app.run()