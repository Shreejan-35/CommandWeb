from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return "login, page"

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/download')
def download():
    return render_template('download.html')


if __name__ == "__main__":
    app.run(debug=True)