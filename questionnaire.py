import json


class Answer:

    def __init__(self, id, answer, acceptable):
        self.id = id
        self.answer = answer
        self.acceptable = acceptable


class Question:

    def __init__(self, id, question, answers, optional=False):
        self.id = id
        self.question = question
        self.answers = answers
        self.optional = optional

    def valid(self):
        """ There must be one acceptable answer for the Question to be acceptable. """
        return any([a.acceptable for a in self.answers])

    def __getitem__(self, key, default=None):
        for a in self.answers:
            if a.id == key:
                return a
        return default

    get = __getitem__


class Questionnaire:

    @classmethod
    def from_json(cls, json_fd):
        d = json.load(json_fd)
        return cls.from_dict(d)

    @classmethod
    def from_json_string(cls, json_str):
        d = json.loads(json_str)
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, q_dict):
        questionnaire = cls(q_dict['id'], q_dict['title'], [])
        
        for q in q_dict['questions']:
            question = Question(q['id'], q['question'], [], q.get('optional', False))
            for a in q['answers']:
                answer = Answer(a['id'], a['answer'], a['acceptable'])
                question.answers.append(answer)
            questionnaire.questions.append(question)
            
        return questionnaire
    
    def __init__(self, id, title, questions):
        self.id = id
        self.title = title
        self.questions = questions

    def valid(self):
        """ All Questions must be valid for the questionnaire to be valid. """
        return all([q.valid() for q in self.questions])

    def __getitem__(self, key, default=None):
        for q in self.questions:
            if q.id == key:
                return q
        return default

    get = __getitem__
    
    def review_for_validity(self, application):
        """ Evaluate an application for validity. All required answers must be present. """
        necessary = set([q for q in self.questions if not q.optional])

        for q in application['questions']:
            question = self.get(q['question'])
            if question:
                necessary.remove(question)

        return len(necessary) == 0
        
    def review_for_acceptability(self, application):
        """ Evaluate an application for acceptabillity. All required answers must be acceptable. """
        acceptable = True

        if self.review_for_validity(application):
            for q in application['questions']:
                question = self.get(q['question'])
                if question:
                    answer = question.get(q['answer'])
                    if answer and not answer.acceptable:
                        acceptable = False
                        break
        else:
            acceptable = False

        return acceptable
