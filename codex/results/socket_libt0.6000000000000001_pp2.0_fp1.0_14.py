import socket
import time
import os
import math

# Socket creation
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()
print("Socket Created")

# Socket binding
sock.bind(("127.0.0.1", 8080))
sock.listen(1)
print("Socket is listening")

# Socket accepting
conn, addr = sock.accept()
print("Connected to", addr)

# Socket sending
while True:
    data = input("Please enter the number of iterations: ")
    if data.isdigit():
        data = int(data)
    else:
        print("You did not enter a number")
        continue

    conn.send(str.encode(str(data)))
    print("Number of iterations", data, "sent")
    time.sleep(1)

    # Socket receiving
    conn.settimeout(15)
    try:
        message = conn.recv(1024).dec
