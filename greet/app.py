from flask import Flask 

app = Flask(__name__)

#  /welcome   Returns “welcome”
@app.route('/welcome')
def welcome_user():
    html = """<h1> WELCOME! </h1>"""
    return html

#***/welcome/home***   Returns “welcome home”
@app.route('/welcome/home')
def welcome_home():
    html = """<h1> WELCOME HOME! </h1>"""
    return html

#***/welcome/back***   Return “welcome back”
@app.route('/welcome/back')
def welcome_back():
    html = """<h1> WELCOME BACK! </h1>"""
    return html