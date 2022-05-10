import socket
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="TCP Client")
parser.add_argument('-s', '--server', help="Enter server IP", required=True)
parser.add_argument('-p', '--port', help="Enter server port", required=True)
args = parser.parse_args()

HOST = args.server
PORT = int(args.port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "Connected to {0}".format(HOST)

while True:
    try:
        msg = raw_input("Enter message: ")
        s.sendall(msg)
        data = s.recv(1024)
        print "Server response: {0}".format(data)
    except KeyboardInterrupt:
        print "\nClosing connection to {0}".format(HOST)
        s.close()
        sys.exit()
