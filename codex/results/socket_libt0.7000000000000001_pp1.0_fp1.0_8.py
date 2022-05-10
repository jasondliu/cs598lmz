import socket
import struct
import sys
import threading
import time

class UDP_Receiver():

    def __init__(self, ip, port=50000):
        self.ip = ip
        self.port = port
        self.sock = None

    def start(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((self.ip, self.port))

            while True:
                # data, addr = self.sock.recvfrom(1024)
                # print("Received data: " + str(data))
                data, addr = self.sock.recvfrom(1024)
                print("received message: %s" % data)
        except Exception as e:
            print("Exception: " + str(e))

if __name__ == "__main__":
    udp_receiver = UDP_Receiver("127.0.0.1")
    udp_receiver.start()
