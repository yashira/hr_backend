from mongoengine import *

class Teacher(Document):
    first_name = StringField(max_length=200, required=True)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "first_name": self.first_name
        }