from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#making databse and cinfiguring it
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable = False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/GetStarted')
def GetStarted():
    return render_template('GetStarted.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)