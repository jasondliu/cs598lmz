import socket
import sys
import time
import thread

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def send_message(socket, message):
    try:
        socket.send(message)
    except socket.error:
        # Send failed
        print 'Send failed'
        sys.exit()

def receive_message(socket):
    reply = socket.recv(4096)
    return reply

def receive_thread(socket):
    while True:
        reply = receive_message(socket)
        print reply

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.
