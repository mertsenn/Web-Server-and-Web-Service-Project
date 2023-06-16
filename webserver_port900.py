from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "WebServer running on port 900"

@app.route("/fibonacci/<int:num>")#this is the route that the user will use to access the fibonacci function
def fibonacci(num):
    response = requests.get("http://localhost:80/fibonacci/{}".format(num))
    return response.text

@app.route("/reverse/<string:text>")#this is the route that the user will use to access the reverse function
def reverse(text):
    response = requests.get("http://localhost:80/reverse/{}".format(text))#requests.get is used to send a get request to the webserver on port 80
    return response.text

if __name__ == "__main__":#this is the main function that will run the webserver
    app.run(port=900)
