import unittest
from final_project import Question, MultipleChoiceQuestion, TrueFalseQuestion, Quiz

class TestQuestion(unittest.TestCase):
    def test_question_validation(self):
        """Testing answer validation for the base Question class"""
        question = Question("Is Northeastern the best university?", ["Yes", "No"], "Yes")
        self.assertTrue(question.validate_answer("Yes"))  # Correct answer
        self.assertFalse(question.validate_answer("No"))  # Wrong answer
    
    def test_mcq_validation(self):
        """Testing answer validation for MCQ"""
        question = MultipleChoiceQuestion("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris")
        self.assertTrue(question.validate_answer("Paris"))  # Correct answer
        self.assertFalse(question.validate_answer("London"))  # Wrong answer

    def test_TF_question_validation(self):
        """Testing answer validation for T/F question"""
        question = TrueFalseQuestion("The Earth is flat.", "False")
        self.assertTrue(question.validate_answer("False"))  # Correct answer
        self.assertFalse(question.validate_answer("True"))  # Wrong anser

class TestQuiz(unittest.TestCase):
    def setUp(self):
        """Quiz with questions for each test"""
        self.questions = [MultipleChoiceQuestion("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"), TrueFalseQuestion("The Earth is round.", "True")]
        self.quiz = Quiz(self.questions)

    def test_initial_state(self):
        """Tetesing the all aspects of initial state of quiz"""
        self.assertEqual(self.quiz.score, 0)  # Starting score should be 0
        self.assertEqual(self.quiz.current_question_index, 0)  # Should start at the first question
        self.assertFalse(self.quiz.is_quiz_over())  # Quiz should not skip to end (ensures questions are asked)

    def test_check_answer(self):
        """Testing for when checking a correct answer"""
        self.assertTrue(self.quiz.check_answer("Paris"))  # Correct answer
        self.assertEqual(self.quiz.score, 1)  # Score should increment by 1
        self.assertFalse(self.quiz.is_quiz_over())  # Quiz should not end after one question

        """Testing end of quiz"""
        self.assertTrue(self.quiz.check_answer("True"))  #Correct answer for second question
        self.assertEqual(self.quiz.score, 2)  # Score should be at 2
        self.assertTrue(self.quiz.is_quiz_over())  # Quiz should end after questions are answered

    def test_check_answer_wrong(self):
        """Testing for when answer is wrong"""
        self.assertFalse(self.quiz.check_answer("London"))  # Wrong answer for the first question
        self.assertEqual(self.quiz.score, 0)  # Score shouldn't increase

        self.assertTrue(self.quiz.check_answer("True"))    # Correct answer for the second question
        self.assertEqual(self.quiz.score, 1)  # Score should be 1

        self.assertTrue(self.quiz.is_quiz_over()) #Quiz = over

if __name__ == '__main__':
    unittest.main()
