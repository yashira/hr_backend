from ariadne import convert_kwargs_to_snake_case
from modules.subject import Subject


@convert_kwargs_to_snake_case
def createSubject_resolver(obj, info, subject_name, description, grade):
    try:
        subject = Subject(
            subject_name = subject_name,
            description = description,
            grade = grade
        )
        subject.save()
        payload = {
            "success": True
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload