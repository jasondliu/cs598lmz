import socket
import sys

#input the ipaddress with port
host = "10.0.0.1"
port = 9999

#create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

