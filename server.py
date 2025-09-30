# we're making a website right now with a backend and frontend. this is called a dynamic site. websites without backends are called static sites 
# https://en.wikipedia.org/wiki/Dynamic_web_page
# https://en.wikipedia.org/wiki/Static_web_page
# to work with python on the backend of a website, we are using a framework called Flask 
# learn more about flask here! https://flask.palletsprojects.com/en/1.1.x/



import os
# import the 4 classes from the flask module
from flask import Flask, request, render_template, jsonify
import markovify

# create the application object
app = Flask(__name__, static_folder='public', template_folder='views')

app.config['TEMPLATES_AUTO_RELOAD'] = True

# @app.route('/') links a function to a url path
# in this case we are telling the webapp, when you get a request from the client for the url '/' (aka home), display the index.html
@app.route('/')
def homepage():
    return render_template('index.html')

# try this out by going to the url for this glitch sketch with a /test at the end of the url!
@app.route('/test')
def testpage():
    return "hi! I'm a message from the backend!"

# this part says when the server gets a request for the url '/generate', trigger our markov chain function to return sentences!
@app.route('/generate')
def generate():

    # now here is our regular python generator!
    # if you want to replace this code, with your own, try either of these:
    # 1. swapping out the source text here (make   sure you add your source to the sketch on the left of the screen)
    # 2. pasting your own code here that returns text instead of just printing it
    
    with open("wordsL.txt") as f:
      text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    # Print five randomly-generated sentences

    sentence_group = []

    for i in range(5):
        sentence = text_model.make_sentence()
        sentence_group.append(sentence)

    # this is the output that's being returned to the frontend!
    return ("\n".join(sentence_group))


# this line start the server with the 'run()' method
if __name__ == '__main__':
    app.run()