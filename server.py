from flask import Flask, request, render_template, jsonify
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
    # return jsonify(
    #     message="Hello World!"
    # )

@app.route("/akhila")
def akhila():
    return "Hi Akhila"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
