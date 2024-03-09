from util.database import DataBase
from modules.subject import Subject

def listSubject_resolver(obj, info):
    database = DataBase()
    database.setConnection()
    try:
        subjects = []
        for subject in Subject.objects:
            subjects.append(subject.to_dict())

        payload = {
            "success": True,
            "subjects": subjects
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

