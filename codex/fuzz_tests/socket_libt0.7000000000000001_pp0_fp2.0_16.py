import socket
import sys
import json
import traceback

class Client(object):

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print("Connected to " + host + ":" + str(port))
        self.id = None

    def run(self):
        try:
            while True:
                self.sock.send(bytes("{}\n", "utf-8"))
                buf = ""
                while "\n" not in buf:
                    buf += self.sock.recv(8).decode("utf-8")
                try:
                    data = json.loads(buf)
                    if "exception" in data:
                        print("EXCEPTION: " + data["exception"])
                        break
                    if "disconnected" in data:
                        print("Disconnected: " + data["disconnected"])
                        break
                    elif "connected" in data:
                        self.id = data["
