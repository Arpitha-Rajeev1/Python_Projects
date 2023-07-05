# Rest API Using Flask and Jsonify in Python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sum/<int:n>')
def sum(n):
    result = n+13
    return jsonify(result)

@app.route('/avg/<int:n>')
def avg(n):
    result = (n+2)/2
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
