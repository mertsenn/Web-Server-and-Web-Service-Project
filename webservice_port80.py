from flask import Flask

app = Flask(__name__)

@app.route("/")#this is the route that the user will use to access the index function
def index():
    return "WebService running on port 80"#this is the message that will be displayed when the user accesses the index function

@app.route("/fibonacci/<int:num>")#this is the route that the user will use to access the fibonacci function
def fibonacci(num):
    fib_list = [0, 1]
    while len(fib_list) < num + 1:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return str(fib_list[num])

@app.route("/reverse/<string:text>")#this is the route that the user will use to access the reverse function
def reverse(text):
    return text[::-1]

if __name__ == "__main__":#this is the main function that will run the webserver
    app.run(port=80)
