import unittest

from questionnaire import Answer, Question


class QuestionTests(unittest.TestCase):

    def setUp(self):
        self.a1 = Answer('1', 'Answer 1', False)
        self.a2 = Answer('2', 'Answer 2', False)
        self.a3 = Answer('3', 'Answer 3', True)
        self.a4 = Answer('4', 'Answer 4', True)

        self.q1 = Question('1', 'Question 1', [self.a1, self.a2])

        self.q2 = Question('2', 'Question 2', [self.a2, self.a3])

        self.q3 = Question('3', 'Question 3', [self.a3, self.a4])

    def test_question_invalidity(self):
        """
        A Question is only valid if at least one Answer is acceptable.
        """
        self.assertFalse(self.q1.valid(), "Question valid despite no acceptable answers")

    def test_question_is_valid(self):
        
        self.assertTrue(self.q2.valid(), "Question not valid despite having an acceptable answer")

    def test_question_can_have_multiple_acceptable_answers(self):
        
        self.assertTrue(self.q3.valid(), "Question not valid despite having only acceptable answers")

    def test_answer_lookup(self):

        self.assertEqual(self.q3.get('3'), self.a3, "Answer lookup can't find proper object")
