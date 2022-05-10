import socket
import sys
from thread import *

# creating a server
HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "Bind failed. Error code: " + str(msg[0]) + ", Message: " + str(msg[1])
    sys.exit()

print "Socket bind complete"

s.listen(10)
print "Socket now listening"


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    conn.send("Welcome to the server. Type something and hit enter\n")
    # infinite loop so that function do not terminate and thread do not end.
    while True:
        # Receiving from client
        data = conn.recv(1024)
        reply = "OK... " + data
        if not data:
            break

        conn.sendall(reply)

