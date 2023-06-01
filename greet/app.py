from flask import Flask 

app = Flask(__name__)


#  /welcome Route ---> returns “welcome”
@app.route('/welcome')
def welcome_user():
    html = """<h1> WELCOME! </h1>"""
    return html

#  /welcome/home Route ---> returns “welcome home”
@app.route('/welcome/home')
def welcome_home():
    html = """<h1> WELCOME HOME! </h1>"""
    return html

# /welcome/back ---> return “welcome back”
@app.route('/welcome/back')
def welcome_back():
    html = """<h1> WELCOME BACK! </h1>"""
    return html