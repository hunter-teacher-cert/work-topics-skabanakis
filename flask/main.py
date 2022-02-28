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

# example of static content
# like an image or including css
@app.route("/image_css")
def image_css():
  return render_template("image_css.html")
  
@app.route("/form_demo",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form_demo.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "12345":
      error = "BAD PASSWORD"
      name=""
    else: 
      error = ""
      
    return render_template("form_demo.html",error=error, name=name)

@app.route("/session_demo")
def session_demo():

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session_demo.html',count = session['count'])
    
app.run(host="0.0.0.0",port=5000,debug=True)