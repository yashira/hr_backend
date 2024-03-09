from mongoengine import connect

class DataBase():
    def __init__(self) -> None:
        self.mongo_db_uri = "mongodb+srv://bmc_staging:H0eGS1VxfPH5NJ3M@cluster0.unskenx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    def setConnection(self):
        connect(host=self.mongo_db_uri, name='staging')