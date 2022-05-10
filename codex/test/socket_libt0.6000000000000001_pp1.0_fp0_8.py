import socket
import sys
import struct
import time

UDP_IP = "10.0.0.2"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

def main():
	while True:
		data, addr = sock.recvfrom(1024)
		print(data)

if __name__ == "__main__":
	main()
