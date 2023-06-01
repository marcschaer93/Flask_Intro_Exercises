from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


##HARDCODED for each operation Function

# @app.route('/add')
# def do_math():
"""add a and b """
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     sum  = f"{a+b}"
    
#     return sum
    

## BETTER
operators = {'add': add, "sub": sub, 'mult': mult, "div": div}


@app.route("/math/<operation>")
def do_math(operation):
    """do a specific operation on a and b out of the operators dictionary """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result  = operators[operation](a,b)
    
    return str(result)


