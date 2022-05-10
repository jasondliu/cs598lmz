import socket
import time
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print( 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
#flag = 0
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        start = time.time()
        while True :
            # Receive the data in small chunks and retransmit it
            #data = connection.recv(64)
            data = connection.recv(4096)
            data_decoded = data.decode("utf-8")
            #print("Recieving: ", data_decoded)
            if data_decoded == "Done" :
                break
            #print("Sending: ", data_
