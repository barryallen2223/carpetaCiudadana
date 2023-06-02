import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime, timedelta, timezone
#from govCarpeta.cryptoKey import generate_unique_key

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('config/credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://govcarpeta-default-rtdb.firebaseio.com/'
})
ref = db.reference('registerCitizen/')
user_ref = ref.child('citizens')

#Inser data
def insertCitizens(id, name, address, email, password, operatorId, operatorName):
    user_ref.push({
        "id": id,
        "name": name,
        "address": address,
        "email": email,
        "password": password,
        "operatorId": operatorId,
        "operatorName": operatorName,
        "isRegistered": False,
        "path": [
            {
                "document": "Welcome.txt",
                "creation_date": "2023-05-15T10:15:00"
            },
        ]
    })

def readCitizens():
    return user_ref.get()

#Update data
""" ct1 = user_ref.child('paths')
ct1.update({
    'folder2': 'folder2.1/folder2.1.2/cedula.pdf'
}) """
# Get a specific register from registerCitizen/citizens based on id and name
def readCitizenByIdAndName(id, name):
    query = user_ref.get()
    result = []
    for key, value in query.items():
        if value.get("id") == id and value.get("name") == name:
            result.append({
                "key": key,
                "data": value
            })
    return result


def readCitizenByEmail(email, password):
    query = user_ref.get()
    result = []
    for key, value in query.items():
        if value.get("email") == email and value.get("password") == password:
            result.append({
                "key": key,
                "data": value
            })
    return result

def updateisRegistered(id, email, password):
    state = False
    query = user_ref.get()
    for key, value in query.items():
        if value.get("id") == id and value.get("email") == email and value.get("password") == password:
            value["isRegistered"] = True
            user_ref.child(key).update(value)
            state = True
            return state
    return state


def updateOperadorData(id, email, password, operatorId, operatorName):
    state = False
    query = user_ref.get()
    for key, value in query.items():
        if value.get("id") == id and value.get("email") == email and value.get("password") == password:
            value["operatorId"] = operatorId
            value["operatorName"] = operatorName
            user_ref.child(key).update(value)
            state = True
            return state
    return state

def updatePath(id, email, password, docName):
    state = False
    query = user_ref.get()
    for key, value in query.items():
        if value.get("id") == id and value.get("email") == email and value.get("password") == password:
            timezone_offset = -5
            utc_now = datetime.now(timezone.utc)
            desired_timezone = timezone(timedelta(hours=timezone_offset))
            current_datetime = utc_now.astimezone(desired_timezone)
            docDate = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")
            
            folderStructure = value['path']
            append_to_list(folderStructure, docName, docDate)
            
            user_ref.child(key).update(value)
            state = True
            return state
    return state

def append_to_list(list_obj, docName, docDate):
    # Create the new item
    new_item = {
        "document": docName,
        "creation_date": docDate
    }
    # Append the new item to the list
    list_obj.append(new_item)


""" 
def addFolderStructure(folder_structure, path):
    folders = path.split('/')
    current_folder = folder_structure
    for i, folder in enumerate(folders):
        if folder not in current_folder:
            current_folder[folder] = {}
        current_folder = current_folder[folder]
        if i == len(folders) - 1:
            if '.' in folder:
                file_name, file_extension = folder.split('.')
                current_folder['docContent'] = 'null'
                current_folder['docTitle'] = folder
                current_folder['isVerified'] = True
    return folder_structure


# Example usage
id = 1234567890
name = "Carlos Andres Caro"

register = getRegisterByIdAndName(id, name)
print(register)

#Select data
handle = db.reference('registerCitizen/')
print(ref.get()) """