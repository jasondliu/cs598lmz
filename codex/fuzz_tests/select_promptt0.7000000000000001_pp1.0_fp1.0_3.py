import select
# Test select.select()
from socket import socket, AF_INET, SOCK_STREAM
import sys
from time import ctime


if len(sys.argv) != 3:
    print('Usage: %s <ipaddr> <port>' % sys.argv[0])
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]

s = socket(AF_INET, SOCK_STREAM)
s.connect_ex((host, port))

# print(s.getpeername())

s.setblocking(0)
s.settimeout(5)
s.send('Hello, world')

while True:
    try:
        data = s.recv(1024)
        if not data:
            break
        print(data)
        break
    except socket.timeout as e:
        print('Receive data timeout:', e)
    except socket.error as e:
        print(ctime(), ':', e)
        break

s.close()
