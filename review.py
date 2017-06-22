import argparse
import json
import os
import os.path

from questionnaire import Questionnaire

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Review applications.')
    parser.add_argument('-q', dest='questionnaire_path', help='Path to the questionnaire JSON file')
    parser.add_argument('-a', dest='applications_directory', help='Directory in which to find the applications')

    args = parser.parse_args()

    with open(args.questionnaire_path, 'r') as q_file:
        questionnaire = Questionnaire.from_json(q_file)

    acceptable, unacceptable = 0, 0
        
    for application_filename in os.listdir(args.applications_directory):
        with open(os.path.join(args.applications_directory, application_filename), 'r') as appl_json:
            application = json.load(appl_json)

        if questionnaire.review_for_acceptability(application):
            acceptable += 1
            print "{} has submitted an acceptable application.".format(application['name'])
        else:
            unacceptable += 1

    print "\n{} acceptable application{}. {} application{} ignored.".format(
        acceptable, '' if acceptable == 1 else 's', unacceptable, '' if unacceptable == 1 else 's')
