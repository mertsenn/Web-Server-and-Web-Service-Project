# Cmpe322 Homework2
## Web Server and Web Service Project

This project consists of three main components: a Web Server (WebServer), a Web Service (WebService), and a Client Browser (Edge or Chrome).

### WebServer (Port 900 and Port 901 with Encryption)

The WebServer is responsible for handling incoming requests from clients. It has two configurations:

- **Port 900:** This configuration serves as a web server without security or encryption.
- **Port 901:** This configuration supports encryption, providing secure communication.

### WebService (Port 80 and Port 443 with Encryption)

The WebService acts as a backend service for the WebServer. It offers the following methods:

- **Fibonacci Calculation:** Given an integer `X`, it calculates the Fibonacci sequence up to `X`.
- **String Reversal:** Given a string `X`, it reverses the characters of the string (e.g., "apple" becomes "elppa").

### Client (Edge or Chrome)

The client, represented by either the Edge or Chrome browser, interacts with the WebService through the WebServer. It can make requests to calculate Fibonacci numbers and reverse strings.

### Technologies Used

- Flask (Python Framework) for building the WebServer and WebService.
- SSL/TLS for encryption and secure communication.
- Requests library for making HTTP requests between components.

### How to Run

1. Start the WebServer:
   - Run the `WebServer.py` file to start the WebServer on port 900 or 901.

2. Start the WebService:
   - Run the `WebService.py` file to start the WebService on port 80 or 443 with encryption.

3. Access the Client:
   - Open your preferred web browser (Edge or Chrome).
   - Use the browser to make requests to the WebService through the WebServer.

This project demonstrates a basic client-server architecture with encryption support and provides functionality for calculating Fibonacci numbers and reversing strings.

### Youtube Link
