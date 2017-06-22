# Snagajob Hiring Tool

## Models

### questionnaire.json

A sample Questionnaire, represented in JSON. Has an internal id, a
position title, and a series of questions, with answers, at least of
one which is an acceptable answer.

### questionnaire.py

Defines the Python models we work with:

#### Answer

Has an id, a textual element, and a boolean designation as to its
acceptability.

#### Question

Has an id, a textual element, and a list of Answers.

A Question is valid so long as any of its Answers are acceptable.

#### Questionnaire

Has an id, a title, and a list of Questions.

A Questionnaire is valid so long as all of its Questions are also
valid.

A Questionnaire can review an application of question/answer pairs for
both validity (all required questions are answered) and for
acceptability (all required questions are answered with accetable
answers).

## Scripts

Command line scripts to exercise the system.

### generate_applications.py

Creates random applications based on a Questionnaire.

#### Usage

```
$ python generate_applicants.py -h
usage: generate_applicants.py [-h] [-q QUESTIONNAIRE_PATH] [-n NUMBER_OF_APPLICATIONS] [-o OUTPUT_DIRECTORY]

Generate random applications.

optional arguments:
  -h, --help            show this help message and exit
  -q QUESTIONNAIRE_PATH
                        Path to the questionnaire JSON file
  -n NUMBER_OF_APPLICATIONS
                        The number of applications to create
  -o OUTPUT_DIRECTORY   Directory in which to save the applications
```

### review.py

Reviews a group of applications for fitness and acceptability against
a Questionnaire, reports back acceptable applications, and the number
of those ignored.

#### Usage

```
$ python review.py -h
usage: review.py [-h] [-q QUESTIONNAIRE_PATH] [-a APPLICATIONS_DIRECTORY]

Review applications.

optional arguments:
  -h, --help            show this help message and exit
  -q QUESTIONNAIRE_PATH
                        Path to the questionnaire JSON file
  -a APPLICATIONS_DIRECTORY
                        Directory in which to find the applications
```

## Tests

### test_questions.py

Tests Question behavior. In particular, whether a given Question is
valid.

### test_questionnaires.py

Tests Questionnaire behavior. Tests both valid Questionnaires, and
acceptable applications.

## Sample Applications

100 randomly-generated sample Applications for the position described
by `questionnaire.json`.

## Future

There are more than a few ways to improve the system. The following
are not meant to be an exhaustive account, but intended for
conversation starters.

### Definition of 'acceptable'

Currently, the questionnaires operate on the assumption that all
questions are multiple choice, and have at least one acceptable
answer. The system provides for optional questions that needn't be
answered, but all questions that are required must be present for the
application to be both valid and acceptable.

### Alternate Clients

At the moment, the models are simple enough and self-contained with
everything they need for validating internal consistency and
validating external applications. This makes it easy for clients to be
written against it. The command line tools provided ensure
correctness, without the overhead of implementing multiple integration
points between database backends, web servers, front end frameworks,
&c.
