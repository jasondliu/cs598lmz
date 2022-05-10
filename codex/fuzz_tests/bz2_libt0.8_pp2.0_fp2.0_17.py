import bz2
bz2.BZ2Compressor()

import socket

def main():

    host = "127.0.0.1"
    port = 12345

    mySocket = socket.socket()
    mySocket.connect((host,port))

    message = input(" -> ")

    while message != 'q':
            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()

            print ('Received from server: ' + data)

            message = input(" -> ")

    mySocket.close()

if __name__ == '__main__':
    main()

import socket
import bz2
bz2.BZ2Compressor()

def main():
    host = "127.0.0.1"
    port = 12345

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv
