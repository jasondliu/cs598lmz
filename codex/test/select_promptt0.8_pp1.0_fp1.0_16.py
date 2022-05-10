import select
# Test select.select()

import socket
import sys

port = 50007
host = 'localhost'

if sys.argv[1:] == ['server']:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Option to reuse addr
    sock.bind((host, port)) # Bind to the server machine and port
    sock.listen(1) # Listen for requests (1 = how many request queue it will hold)

    while True: # Wait for next request
        print('Listening at', sock.getsockname()) # Prints the address of the server
        sc, sockname = sock.accept() # Connect
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024) # Receive up to 1024 characters
            if not data:
                break
