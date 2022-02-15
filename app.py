from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/overview/')
def overview():
    return render_template('overview.html')

@app.route('/GetStarted/')
def GetStarted():
    return render_template('GetStarted.html')


if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0')