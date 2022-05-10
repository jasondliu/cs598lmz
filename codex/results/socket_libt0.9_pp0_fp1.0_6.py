import socket
import sys
import struct
import time

def main():
    proxy = Proxy()
    proxy.start_proxy()

class Proxy:
    # the magic numbers and protocol are required for properly opening the UDP socket
    magic_number = '\xb5\x62'
    protocol_version = '\x06\x00'
    udp_port = 7003
    ttl = 200
    target_ip = "192.168.0.31"

    #attempt to open a connection with the UDP port
    def __init__(self):
        # this is to run the UDP port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto("x", ('<broadcast>', self.udp_port))
        s.close()

    def start_proxy(self):
        try:
            #open the socket and establish a connection
            udp
