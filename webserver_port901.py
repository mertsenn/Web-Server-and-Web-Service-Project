from flask import Flask, request
import requests
import ssl

app = Flask(__name__)

@app.route("/")#this is the route that the user will use to access the index function
def index():
    return "WebServer running on port 901 with encryption"
@app.route("/service/fibonacci/<int:num>")#this is the route that the user will use to access the fibonacci function
def fibonacci(num):
    response = requests.get("https://localhost:443/fibonacci/{}".format(num), verify=False)
    return response.text
#
@app.route("/service/reverse/<string:text>")#this is the route that the user will use to access the reverse function
def reverse(text):
    response = requests.get("https://localhost:443/reverse/{}".format(text), verify=False)#requests.get is used to send a get request to the webserver on port 443
    return response.text

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)#ssl.SSLContext is used to create a context object that will be used to load the certificate and key files
    context.load_cert_chain("cert.pem", "key.pem")#context.load_cert_chain is used to load the certificate and key files
    app.run(port=901, ssl_context=context)#ssl_context is used to specify the certificate and key files
