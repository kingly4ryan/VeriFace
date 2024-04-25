import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://prox-e-19fd2-default-rtdb.firebaseio.com/"
})
 
ref = db.reference('Students')
 
data = {
    "12101700":
        {
        "name": "Hrithik Roshan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34" 
        },
    "12113186":
        {
        "name": "Zendaya",
        "major": "Economics",
        "starting_year": 2018,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34" 
        },
    "12200582":
        {
        "name": "Shriya Thakur",
        "major": "Fashion Designing",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34" 
        },
    "12108819":
        {
        "name": "Nishtha Sharma",
        "major": "CSE",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34" 
        }

}
for key, value in data.items():
    ref.child(key).set(value)
