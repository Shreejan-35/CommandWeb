from typing import final
import pyrebase
from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#making databse and cinfiguring it
config = {
    "apiKey": "AIzaSyA10S3-yjJ-x7qAYnrbJc07gbMK17Xjkts",
    "authDomain": "commandconsoleuser.firebaseapp.com",
    "databaseURL": "https://commandconsoleuser-default-rtdb.firebaseio.com",
    "projectId": "commandconsoleuser",
    "storageBucket": "commandconsoleuser.appspot.com",
    "messagingSenderId": "217715886011",
    "appId": "1:217715886011:web:b68a9ef60117a02957669e",
    "measurementId": "G-6DM8EW6RM2"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/GetStarted')
def GetStarted():
    return render_template('GetStarted.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        if request.form['submit'] == "add":
            username = request.form['username']
            password = request.form['password']
            db.child("users").child("usersList").child(username).push({username:password})
        
        elif request.form['submit'] == "delete":
            username = request.form['username']
            password = request.form['password']
            db.child("users").child("usersList").child(username).remove()

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)