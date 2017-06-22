import json


class Answer:

    def __init__(self, id, answer, acceptable):
        self.id = id
        self.answer = answer
        self.acceptable = acceptable


class Question:

    def __init__(self, id, question, answers):
        self.id = id
        self.question = question
        self.answers = answers

    def valid(self):
        """ There must be one acceptable answer for the Question to be acceptable. """
        return any([a.acceptable for a in self.answers])

    def __getitem__(self, key, default=None):
        for a in self.answers:
            if a.id == key:
                return a
        return default
    

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
            question = Question(q['id'], q['question'], [])
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
    
    def validate(self, application):
        """ Evaluation an application for acceptance. All answers must be acceptable. """
        acceptable = True
        
        for q in application['questions']:
            question = self[q['question']]
            if question:
                answer = question[q['answer']]
            if not answer.acceptable:
                acceptable = False
                break

        return acceptable
