import socket
import os

print("Attempting to connect to server...")

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 1234))
        print("Connected!")
        break
    except socket.error:
        print("Failed to connect, retrying in 3 seconds...")
        time.sleep(3)

while True:
    try:
        s.send(bytes(input(">>> "), "utf-8"))
        os.system("clear")
        print(s.recv(4096).decode("utf-8"))
    except KeyboardInterrupt:
        print("\nDisconnected!")
        break
