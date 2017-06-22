import unittest

from questionnaire import Answer, Question


class QuestionTests(unittest.TestCase):

    def test_question_validity(self):
        """
        A Question is only valid if at least one Answer is acceptable.
        """

        a1 = Answer('1', 'Answer 1', False)
        a2 = Answer('2', 'Answer 2', False)
        a3 = Answer('3', 'Answer 3', True)
        a4 = Answer('4', 'Answer 4', True)

        q1 = Question('1', 'Question 1', [a1, a2])

        self.assertFalse(q1.valid(), "Question valid despite no acceptable answers")

        q2 = Question('2', 'Question 2', [a2, a3])

        self.assertTrue(q2.valid(), "Question not valid despite having an acceptable answer")

        q3 = Question('3', 'Question 3', [a3, a4])

        self.assertTrue(q3.valid(), "Question not valid despite having only acceptable answers")
