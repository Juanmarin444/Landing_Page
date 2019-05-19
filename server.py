from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/ninjas')

def ninja_info():
    return render_template('ninja.html')

@app.route('/dojos/news')

def dojo_news():
    return render_template('dojo.html')

app.run(debug=True)
