import select
import socket
import sys

from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432
LOG_FILE = "server.log"
CONNECTION_DICT = {}

def log(message):
    """ Appends message to LOG_FILE """
    with open(LOG_FILE, 'a') as f:
        f.write(message + "\n")

def broadcast(msg):
    """ Sends message to all connected clients """
    for client_socket in CONNECTION_DICT.keys():
        client_socket.send(bytes(msg, "utf8"))

def main():
    """ Main function """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f"Server started at {HOST}:{PORT}")
            log(f"Server started at {HOST}:{PORT}")

            while True:
                readable,
