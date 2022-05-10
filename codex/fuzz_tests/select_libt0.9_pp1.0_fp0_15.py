import select
import socket
import struct

# A simple TCP server that discards received data. Use a combination of Tcpdump
# and `netstat -s` to measure how much data is queued inside the kernel at any
# given moment.
#
# $ python3 tcp-discard-server.py &
# $ sudo tcpdump -w - 'host 127.0.0.1 and port 12345' 2>/dev/null |
# > (wc -c; sleep 1; wc -c)
# 1856
# 18816

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', 12345))
    sock.listen(0)

    client_socket, _ = sock.accept()

    try:
        while True:
            f = select.select([client_socket], [], [])[0]
            if not f:
               
