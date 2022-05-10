import socket
import hashlib
import time

def mySHA1(plain):
    return hashlib.sha1(plain.encode('utf-8')).hexdigest()

# how long do i want to wait to terminate my application?
TIME_TO_WAIT = 10

# host = '127.0.0.1'  # Standard loopback interface address (localhost)
host = '192.168.1.105'  # Standard loopback interface address (localhost)
# host = '172.0.0.1'  # Standard loopback interface address (localhost)
# host = '10.0.0.1'  # Standard loopback interface address (localhost)
# host = '0.0.0.0'  # Standard loopback interface address (localhost)
port = 61098        # Port to listen on (non-privileged ports are > 1023)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn,
