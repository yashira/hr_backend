from mongoengine import connect
from modules.teacher import Teacher

mongo_db_uri = "mongodb+srv://bmc_staging:H0eGS1VxfPH5NJ3M@cluster0.unskenx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect(host=mongo_db_uri, name='staging')

def listTeacher_resolver(obj, info):
    try:
        teachers = []
        for teacher in Teacher.objects:
            print(teacher.first_name)
            teachers.append(teacher.to_dict())

        payload = {
            "success": True,
            "teachers": teachers
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

