import json
import unittest

from questionnaire import Answer, Question, Questionnaire

INVALID_QUESTIONNAIRE = dict(
    id="1",
    title="Position 1",
    questions=[
        dict(
            id="1",
            question="Questionnaire Question 1",
            answers=[
                dict(
                    id="1.1",
                    answer="Answer 1.1",
                    acceptable=False),
                dict(
                    id="1.2",
                    answer="Answer 1.2",
                    acceptable=False),
                dict(
                    id="1.3",
                    answer="Answer 1.3",
                    acceptable=False)
            ]),
        dict(
            id="2",
            question="Questionnaire Question 2",
            answers=[
                dict(
                    id="2.1",
                    answer="Answer 2.1",
                    acceptable=False),
                dict(
                    id="2.2",
                    answer="Answer 2.2",
                    acceptable=False),
                dict(
                    id="2.3",
                    answer="Answer 2.3",
                    acceptable=False)
            ])
])

VALID_QUESTIONNAIRE = dict(
    id="1",
    title="Position 1",
    questions=[
        dict(
            id="1",
            question="Questionnaire Question 1",
            answers=[
                dict(
                    id="1.1",
                    answer="Answer 1.1",
                    acceptable=True),
                dict(
                    id="1.2",
                    answer="Answer 1.2",
                    acceptable=False),
                dict(
                    id="1.3",
                    answer="Answer 1.3",
                    acceptable=False)
            ]),
        dict(
            id="2",
            question="Questionnaire Question 2",
            answers=[
                dict(
                    id="2.1",
                    answer="Answer 2.1",
                    acceptable=True),
                dict(
                    id="2.2",
                    answer="Answer 2.2",
                    acceptable=False),
                dict(
                    id="2.3",
                    answer="Answer 2.3",
                    acceptable=False)
            ])
    ])

INVALID_APPLICATION = dict(
    name="invalid",
    questions=[
        dict(
            question="2",
            answer="2.1")
    ])

UNACCEPTABLE_APPLICATION = dict(
    name="invalid",
    questions=[
        dict(
            question="1",
            answer="1.2"),
        dict(
            question="2",
            answer="2.1")
    ])

ACCEPTABLE_APPLICATION = dict(
    name="invalid",
    questions=[
        dict(
            question="1",
            answer="1.1"),
        dict(
            question="2",
            answer="2.1")
    ])


class QuestionnaireTests(unittest.TestCase):

    def test_invalid_questionnaire(self):
        """
        No question in a questionnaire can have only unacceptable answers.
        """
        questionnaire = Questionnaire.from_dict(INVALID_QUESTIONNAIRE)
        self.assertFalse(questionnaire.valid(), "None of the questions are invalid")

    def test_valid_questionnaire(self):
        """
        Every question in a questionnaire must have one acceptable answer.
        """
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        self.assertTrue(questionnaire.valid(), "Some of the questions are invalid")

    def test_questionnaire_length(self):
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        self.assertEqual(len(questionnaire.questions), 2, "Doesn't have two questions")

    def test_application_validity(self):
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        self.assertFalse(questionnaire.review_for_validity(INVALID_APPLICATION), "Questionnaire improperly validates")
        
    def test_application_unacceptability(self):
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        self.assertFalse(questionnaire.review_for_acceptability(UNACCEPTABLE_APPLICATION), "Questionnaire improperly judges unacceptability")

    def test_application_acceptability(self):
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        self.assertTrue(questionnaire.review_for_acceptability(ACCEPTABLE_APPLICATION), "Questionnaire improperly judges acceptability")

    def test_questionnaire_lookup(self):
        questionnaire = Questionnaire.from_dict(VALID_QUESTIONNAIRE)
        q1 = questionnaire.questions[0]
        self.assertEqual(questionnaire.get('1'), q1, "Question lookup by key not working")
