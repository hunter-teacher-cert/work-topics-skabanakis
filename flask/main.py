from flask import Flask, render_template

import random

app = Flask(__name__)

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

@app.route("/")
def index():
  return "<h1>Hello World from my computer !</h1>"

@app.route('/')
@app.route('/dic')
def dict():
    user = {'username': 'Miguel'}
    return render_template('dictionary.html', title='Home', user=user)

@app.route('/conditional')
def conditional():
  user= {"username" : "Moist"}
  return render_template('conditionals.html', title='Home', user=user)


#loops
@app.route('/')
@app.route('/loops')
def loops():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('loops.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/inher')
def inher():
    user = {'username': 'steph'}
    posts = [
        {
            'author': {'username': 'willy'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


    
app.run(host="0.0.0.0",port=5000,debug=True)