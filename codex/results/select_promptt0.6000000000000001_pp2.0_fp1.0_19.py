import select
# Test select.select()
# Polling a socket for readability
#
#

import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8001))

while True:
    inputready, outputready, exceptready = select.select([sock], [], [])
    if inputready:
        data = sock.recv(4096)
        if data:
            print(data)
        else:
            break
    else:
        print('No data received')
        break

sock.close()
