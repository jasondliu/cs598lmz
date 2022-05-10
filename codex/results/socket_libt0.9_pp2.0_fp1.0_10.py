import socket
import sys

if __name__ == '__main__':
    listen_host = "127.0.0.1"
    listen_port = 54321
    if len(sys.argv) > 1:
        listen_host = sys.argv[1]
    if len(sys.argv) > 2:
        listen_port = int(sys.argv[2])
    
    sock = socket.socket()
    
    sock.bind((listen_host, listen_port))
    sock.listen(1)
    print(f"Serving UDP socket on {sock.getsockname()[0]}:{sock.getsockname()[1]}")
    (connection, address) = sock.accept()
    print(f"New Connection from {address[0]}:{address[1]}")
    
    packetLength = 0
    packetStr = ''
    packetIter = 0
    while True:
        data = connection.recv(1024)
        if data:
            packetStr += data.hex()
            if packetStr[packetIter]
