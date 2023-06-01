from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

##HARDCODED for each operation Function. 
@app.route('/add')
def add():
    """ Add a and b and return sum as a string """
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum  = f"{a+b}"
    
    return sum
    

## BETTER Version
operators = {'add': add, "sub": sub, 'mult': mult, "div": div}

@app.route("/math/<operation>")
def do_math(operation):
    """ Do a specific operation on "a" and "b" out of the operators dictionary """
   
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result  = operators[operation](a,b)
    
    return str(result)


