from mongoengine import *

class Subject(Document):
    subject_name = StringField(max_length=200, required=True)
    description = StringField(max_length=500, required=False)
    grade = IntField(min_value=1, max_value=13, required=True)


    def to_dict(self):
        return {
            "id": str(self.pk),
            "subject_name": self.subject_name,
            "description": self.description,
            "grade": self.grade
        }