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
