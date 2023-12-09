import unittest
from final_project import Question, MultipleChoiceQuestion, TrueFalseQuestion, Quiz, load_questions_from_file

class TestQuestion(unittest.TestCase):
    def test_multiple_choice_question_validation(self):
        question = MultipleChoiceQuestion("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris")
        self.assertTrue(question.validate_answer("Paris"))
        self.assertFalse(question.validate_answer("London"))

    def test_true_false_question_validation(self):
        question = TrueFalseQuestion("The Earth is flat.", "False")
        self.assertTrue(question.validate_answer("False"))
        self.assertFalse(question.validate_answer("True"))

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.questions = [
            MultipleChoiceQuestion("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
            TrueFalseQuestion("The Earth is round.", "True")
        ]
        self.quiz = Quiz(self.questions)

    def test_initial_state(self):
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_question_index, 0)
        self.assertFalse(self.quiz.is_quiz_over())

    def test_check_answer(self):
        self.assertTrue(self.quiz.check_answer("Paris"))
        self.assertEqual(self.quiz.score, 1)
        self.assertFalse(self.quiz.is_quiz_over())

        self.assertTrue(self.quiz.check_answer("True"))
        self.assertEqual(self.quiz.score, 2)
        self.assertTrue(self.quiz.is_quiz_over())

    def test_check_answer_incorrect(self):
        self.assertFalse(self.quiz.check_answer("London"))
        self.assertEqual(self.quiz.score, 0)
        self.assertFalse(self.quiz.is_quiz_over())

        self.quiz.check_answer("True")
        self.assertFalse(self.quiz.check_answer("False"))
        self.assertEqual(self.quiz.score, 1)
