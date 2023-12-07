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

def run_quiz(filename):
    category = input("Select a category (easy/hard): ").lower()
    while category not in ['easy', 'hard']:
        print("Invalid category. Please choose 'easy' or 'hard'.")
        category = input("Select a category (easy/hard): ").lower()

    questions = load_questions_from_file(filename, category)
    quiz = Quiz(questions)

    while quiz.has_questions_left():
        current_question = quiz.get_next_question()
        current_question.display_question()
        user_answer = input("Your answer: ")
        quiz.check_answer(user_answer)

    print(f"Congrats, Your final score is: {quiz.score}!")

run_quiz('final_project_2140/quiz_questions.json')
