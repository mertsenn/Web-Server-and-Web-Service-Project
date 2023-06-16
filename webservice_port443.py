from flask import Flask

app_service = Flask(__name__)

@app_service.route("/")#this is the route that the user will use to access the index function
def index():
    return "WebService running on port 443 with encryption"

@app_service.route("/fibonacci/<int:num>")#this is the route that the user will use to access the fibonacci function
def fibonacci(num):
    # Fibonacci logic
    a, b = 0, 1
    fib_sequence = [a, b]
    for _ in range(num - 2):
        a, b = b, a + b
        fib_sequence.append(b)
    return str(fib_sequence)

@app_service.route("/reverse/<string:text>")#this is the route that the user will use to access the reverse function
def reverse(text):
    # String reversal logic
    reversed_text = text[::-1]
    return reversed_text

if __name__ == "__main__":
    app_service.run(port=443, ssl_context=("cert.pem", "key.pem"))#ssl_context is used to specify the certificate and key files
