import socket
import sys
import os
import time
import datetime
import argparse

#set up command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="The port number to listen on", type=int)
parser.add_argument("-d", "--directory", help="The directory to serve files from", default=".")
args = parser.parse_args()

#check port number is valid
if args.port:
    if args.port < 0 or args.port > 65535:
        print("Invalid port number")
        exit(1)
else:
    print("Port number not provided")
    exit(1)

#check directory is valid
if args.directory:
    if not os.path.isdir(args.directory):
        print("Invalid directory")
        exit(1)

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('localhost', args.port)
print
