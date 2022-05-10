import socket
import sys
import time
import threading

if __name__ == '__main__':
    # Capturing the port number from the command line
    serverPort = int(sys.argv[1])

    # Create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    serverSocket.bind(('', serverPort))

    # Start listening on the socket
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print('Connected to: ', addr)

        try:
            message = connectionSocket.recv(1024)
            print('Message: ', message)

            filename = message.split()[1]
            print('File name: ', filename)

            f = open(filename[1:])
            outputdata = f.read()

            # Send one HTTP header line into socket
            connectionSocket.send(b'HTTP/1.1 200 OK\
