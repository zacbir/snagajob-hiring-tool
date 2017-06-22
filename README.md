# Snagajob Hiring Tool

## Models

### questionnaire.json

A sample Questionnaire, represented in JSON. Has an internal id, a
position title, and a series of questions, with answers, at least one
of which is an acceptable answer.

### questionnaire.py

Defines the Python models we work with:

#### Answer

Has an id, a textual element, and a boolean designation as to its
acceptability.

#### Question

Has an id, a textual element, a list of Answers, and a boolean
designating the question as optional, defaulting to False (i.e.,
required by default).

A Question is valid so long as any of its Answers are acceptable.

#### Questionnaire

Has an id, a title, and a list of Questions.

A Questionnaire is valid so long as all of its Questions are also
valid.

A Questionnaire can review an application of question/answer pairs for
both validity (all required questions are answered) and for
acceptability (all required questions are answered with acceptable
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
valid, and whether answer lookup by id works as intended.

### test_questionnaires.py

Tests Questionnaire behavior. Tests Questionnaire validation and
question lookup by id, and vetting applications for acceptability.

## Sample Applications

100 randomly-generated sample Applications for the position described
by `questionnaire.json`.

## Sample Output

```
$ python review.py -q ./questionnaire.json -a ./applications
0859852d-1e0a-49f7-b99e-09ac9f9ffa08 has submitted an acceptable application.
0d383b70-2772-4c2e-9620-a57b1f731f19 has submitted an acceptable application.
16dcc3c9-3c02-410a-b061-f835060d9746 has submitted an acceptable application.
262a8681-a1fb-4afd-a631-b62838d9fbf2 has submitted an acceptable application.
281bbb00-2798-4b8b-9add-2bb0c22170f7 has submitted an acceptable application.
31d6a530-52ba-48ec-a12d-6fd063a85210 has submitted an acceptable application.
52207d6d-afba-404b-a0c6-7420a8213ef2 has submitted an acceptable application.
54ab4482-ba67-4093-a52e-7fa24ef69e9f has submitted an acceptable application.
58b57e70-68f1-458e-a6b4-02bef9189e18 has submitted an acceptable application.
5f9141c3-7d81-4cf5-b778-a2afb3131183 has submitted an acceptable application.
66d1bf71-f126-426c-a5d1-e431b7e3b291 has submitted an acceptable application.
71ee36e5-3258-40da-9091-973a1e1324dd has submitted an acceptable application.
72f66c69-1ea2-4cf9-ab88-fd6ce0b0ed65 has submitted an acceptable application.
73c46b2a-f710-4fb2-a570-f2bf0982f109 has submitted an acceptable application.
8bcd9685-3d54-48f1-b657-4940ac10f190 has submitted an acceptable application.
8c6b177d-faf5-406f-9fd8-43ba8c576ee3 has submitted an acceptable application.
a6a4a920-0af6-4e63-8681-b9b98ee81f68 has submitted an acceptable application.
a6f5f27b-581f-4f06-b9fc-d6cb8f130ef0 has submitted an acceptable application.
b50b26b1-3692-45b5-b180-ba0a5493b463 has submitted an acceptable application.
b548e21c-8d7e-4ba2-96fc-916784b9d780 has submitted an acceptable application.
b659086a-9735-46df-b022-a576df25a943 has submitted an acceptable application.
c1aea164-d3a7-423e-9aaa-a5c182dcd3ab has submitted an acceptable application.
c2f368ce-ea47-42a9-85a2-d8086b5ef2d5 has submitted an acceptable application.
c30a0002-f318-4f6f-b353-1e7bcc34bbf6 has submitted an acceptable application.
c85650be-6144-4687-b4b2-f7bbfdbe2cd6 has submitted an acceptable application.
d851c26d-11ae-48e9-b389-e5ebf539b4f5 has submitted an acceptable application.
d9b059d3-ccca-4d48-bf62-d9586f2214b6 has submitted an acceptable application.
da128362-992a-4390-8814-73a27c94ee46 has submitted an acceptable application.
db4247df-82f7-4c3f-b02a-f1d734366c35 has submitted an acceptable application.
ef5850df-ac30-42f6-82e6-c8c711087857 has submitted an acceptable application.
f28e7d9c-e659-4a8f-a29a-ec7d8da0af40 has submitted an acceptable application.

31 acceptable applications. 69 applications ignored.
```

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
