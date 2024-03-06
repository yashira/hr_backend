from mongoengine import *

class Subject(Document):
    subject_name = StringField(max_length=200, required=True)
    description = StringField(max_length=500, required=False)
    grade = StringField(max_length=500, required=True)


    def to_dict(self):
        return {
            "id": str(self.pk),
            "subjectName": self.subject_name,
            "description": self.description,
            "subjectName": self.grade
        }