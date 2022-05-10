import socket
import sys

from util import get_host_ip

def send_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = get_host_ip()
    server_address = (ip, 10000)

    sock.connect(server_address)
    try:
        sock.sendall(message.encode())
    finally:
        sock.close()

if __name__ == '__main__':
    send_message(sys.argv[1])
