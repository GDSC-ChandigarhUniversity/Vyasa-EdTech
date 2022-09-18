import requests
import pyrebase
import requests

config = {
    "apiKey" : "api-key",
    "authDomain" : "auth domain-1.firebaseapp.com",
    "databaseURL" : "database-url",
    "projectId" : "project_ID-1",
    "storageBucket" : "bucket",
    "messagingSenderId" : "messenger id",
    "appId" : "app id",
    "measurementId" : "Measurement id",
    "serviceAccount": "service_acc.json"
}

print("""
<!DOCTYPE html>
<html lang="en">
  
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content=
        "width=device-width, initial-scale=1.0">
    <title>navbar</title>
    <style>
        ul {
            list-style-type: none;
            margin-top : 10px ;
            padding-left : 20px;
            padding-right : 20px;
            border-radius : 25px;
            overflow: hidden;
           height : 80vh;
           overflow-y:scroll;
        }
  
        li {
            
               background-color: white;
    margin: 20px;
    
    align-content: center;
    color: black;
    padding: 10px;
    box-shadow: 5px 10px;
        }
  
        li a {
            display: block;
            color: black;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            
        }
  
        li a:hover {
            background-color: lightgreen;
            color: black;
        }
        work {
           text-align:center;
           font-weight:500;
           color: black;
        }
        body{
        background-color:#caecfd;
        }
        work h3{
             text-align: center;
        }
    </style>
</head>
  
<body>
   <div class ="work" ><h3> VIDEOS </h3> </div>
   
    <ul>
""")

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
files = storage.child("images").list_files()
for file in files:
    file1 = open('files_to_download.txt', 'r')
    Lines = file1.readlines()
    count = 0

    
    for line in Lines:
        count += 1
        temp = line.strip()
        name = line.replace("bucket url", "")
        nameofthefile = file.name
        z = storage.child(file.name).get_url(None)
        new_name = name.replace("%2F","%252F")
        new_name2 = new_name.replace("%20","%2520")
        new_name3 = new_name2.replace("?alt=media","%3Falt%3Dmedia%0A")
        #print(new_name3)


        print('<li><a href="http://192.168.234.196:8000/'+ new_name3 +".mp4"+ '"' + '>'+"Chapter"+'<li>')
print("""
</ul>
</body>
</html>
""")
