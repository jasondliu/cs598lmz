import socket
import sys

SERVER_ADDRESS = ''
SERVER_PORT = 65000

message = 'hello,world'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message,(SERVER_ADDRESS,SERVER_PORT))
