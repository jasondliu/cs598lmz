import select
# Test select.select()

# Check if a socket is readable
def readable(sock):
    try:
        return select.select([sock], [], [], 0) == ([sock], [], [])
    except select.error:
        return False

# Check if a socket is writable
def writable(sock):
    try:
        return select.select([], [sock], [], 0) == ([], [sock], [])
    except select.error:
        return False

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org', 80))

print(readable(s))
print(writable(s))
