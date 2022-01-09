from typing import final
from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#making databse and cinfiguring it
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable = False)

    def __repr__(self) -> str:
        return f"{self.username} - {self.password}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/GetStarted')
def GetStarted():
    return render_template('GetStarted.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    IsUser = None
    IsPassword = None
    UserName = None
    finalList= []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        validUsername = Users.query.filter_by(username=username).first()
        validPassword = Users.query.filter_by(password=password).first()
        if(validUsername != None):
       
            if(validPassword != None):
                IsUser = "True"
                IsPassword = "True"
                UserName = validUsername
            else:
                IsUser="False"
                IsPassword="False"
        else:
            IsUser = "False"
        
        finalList.append(IsUser)
        finalList.append(IsPassword)
        finalList.append(username)
        
    return render_template('login.html', finallist = finalList)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = Users(username=username, password=password)
        db.session.add(users)
        db.session.commit()
        
    allUsers = Users.query.all()
    print(allUsers)
    return render_template('register.html', allUsers = allUsers)


if __name__ == "__main__":
    app.run(debug=True)