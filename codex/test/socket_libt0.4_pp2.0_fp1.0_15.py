import socket
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 client.py <host>:<port>")
        return
    host, port = sys.argv[1].split(':')
    port = int(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    try:
        while True:
            data = input("Enter data: ")
            sock.sendall(data.encode('utf-8'))
            data = sock.recv(1024)
            print("Received: {}".format(data.decode('utf-8')))
    finally:
        sock.close()

if __name__ == "__main__":
    main()
