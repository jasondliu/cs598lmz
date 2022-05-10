import socket
import random
import time
import sys

log_level = 2

def log(text, level=1):
    if log_level >= level:
        print(text)

listen_port = 1337

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', listen_port))

    while True:
        data, addr = sock.recvfrom(1024)
        log(data)

        if data == b'ping':
            sock.sendto(b'pong', addr)

        elif data == b'hello':
            sock.sendto(b'hi', addr)

        elif data == b'sleep':
            time.sleep(random.randint(1, 10))

        elif data == b'shutdown':
            sys.exit(0)

        else:
            sock.sendto(b'unknown command', addr)

if __name__ == '__main__':
    main()
