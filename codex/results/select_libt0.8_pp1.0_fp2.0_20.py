import select
import socket
import struct
import sys

#HOST = sys.argv[1]
HOST = "127.0.0.1"
PORT = 5000

print('Client: start to connect')
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except socket.error as e:
    print('Client:', e)
    sys.exit(1)

sock.setblocking(False)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

# Send data
while True:
    message = input('Client: Input >> ')

    sock.sendall(message.encode('utf-8'))
    # Look for the response
    amount_received = 0
