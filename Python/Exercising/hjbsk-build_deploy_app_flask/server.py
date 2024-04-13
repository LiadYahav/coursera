from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")


@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = str(summation(num1, num2))
    except TypeError:
        return {"error message": "This app only supports numeric values"}
    else:
        return result


@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = str(subtraction(num1, num2))
    except TypeError:
        return {"error message": "This app only supports numeric values"}
    else:
        return result


@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = str(multiplication(num1, num2))
    except TypeError:
        return {"error message": "This app only supports numeric values"}
    else:
        return result


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
