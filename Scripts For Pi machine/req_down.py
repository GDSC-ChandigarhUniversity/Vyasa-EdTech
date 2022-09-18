import requests
import pyrebase
import requests

config = {
    "apiKey" : "api-key",
    "authDomain" : "domain",
    "databaseURL" : "database-url",
    "projectId" : "project id",
    "storageBucket" : "your bucket",
    "messagingSenderId" : "sender id",
    "appId" : "app id",
    "measurementId" : "i=measurement id",
    "serviceAccount": "service_acc.json"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
files = storage.list_files()


for file in files:
    nameofthefile = file.name
    z = storage.child(file.name).get_url(None)
    print(z)

