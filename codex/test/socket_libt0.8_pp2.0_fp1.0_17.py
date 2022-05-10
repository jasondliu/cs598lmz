import socket
import time

# TCP_IP = '192.168.1.1'
# TCP_IP = '127.0.0.1'
# TCP_IP = '192.168.0.100'
TCP_IP = '192.168.43.65' #WIFI
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.settimeout(1.0)

