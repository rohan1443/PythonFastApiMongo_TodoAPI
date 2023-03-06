from pymongo import MongoClient

client  = MongoClient('mongodb+srv://rohan1443:Pa55word@cluster0.oybkelq.mongodb.net/?retryWrites=true&w=majority', tls=True,
                             tlsAllowInvalidCertificates=True)

db = client.todo_application

collection_name = db['todos_app']