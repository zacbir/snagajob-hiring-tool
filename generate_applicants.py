import argparse
from datetime import datetime
import json
import os.path
import random
import uuid

from questionnaire import Answer, Question, Questionnaire

def generate_application_from(questionnaire):
    should_force_acceptable = random.choice((True, False, False))
    
    applicant_name = str(uuid.uuid4())
    application_date = datetime.today().isoformat()

    questions = []
    
    for question in questionnaire.questions:
        if should_force_acceptable:
            answer = random.choice([a for a in question.answers if a.acceptable])
        else:
            answer = random.choice(question.answers)
        questions.append(dict(question=question.id, answer=answer.id))

    return "{}-{}.json".format(applicant_name, application_date), dict(name=applicant_name, questions=questions)
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate random applications.')
    parser.add_argument('-q', dest='questionnaire_path', help='Path to the questionnaire JSON file')
    parser.add_argument('-n', dest='number_of_applications', help='The number of applications to create', type=int)
    parser.add_argument('-o', dest='output_directory', help='Directory in which to save the applications')

    args = parser.parse_args()

    with open(args.questionnaire_path, 'r') as q_file:
        questionnaire = Questionnaire.from_json(q_file)

    for i in range(args.number_of_applications):
        output_filename, filled_questionnaire = generate_application_from(questionnaire)

        with open(os.path.join(args.output_directory, output_filename), 'w') as questionnaire_outfile:
            json.dump(filled_questionnaire, questionnaire_outfile, indent=4)
