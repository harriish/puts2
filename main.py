from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add', methods=['GET','POST'])#GET and POST are a list of HTTP methods GET means we retrieve the elements and POST means to add an element
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    result = value1 + value2
    C = str(result).split('/')
    if len(C)==2:
	D = float(C[0])/float(C[1])
	E = str(D).split(".")
	if E[1] == '0':
		return " %s\n" % E[0]
	else:
		return " %s\n" %D
    else:
	F = str(result).split(".")
	return "%s \n" % F[0]


if __name__ == "__main__":
    app.run()
