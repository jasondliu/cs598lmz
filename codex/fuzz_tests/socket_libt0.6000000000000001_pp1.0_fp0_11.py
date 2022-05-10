import socket
import sys
import json
import time

f = open("config.json", "r")
config = json.loads(f.read())
f.close()

def main():
    host = config["server_address"]
    port = config["server_port"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        sock.sendall(b"Hello, world")
        data = sock.recv(1024)
        print("Received", repr(data))
        time.sleep(1)

if __name__ == "__main__":
    main()
