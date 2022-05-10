import select
# Test select.select
import socket
# Connect to the socket
server_address = ('localhost', 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(0)
msg = 'hello, world!'
total_sent = 0
while total_sent < len(msg):
    sent = sock.send(msg[total_sent:])
    if sent == 0:
        raise RuntimeError('socket connection broken')
    total_sent = total_sent + sent
    # Wait for the socket to be writeable
    while True:
        (rw, ww, ew) = select.select([], [sock], [], 1)
        if ww:
            break
# Wait for the socket to be readable
while True:
    (rw, ww, ew) = select.select([sock], [], [], 1)
    if rw:
        break
# Read the response
data = sock.recv(16)
print('received "%s"' % data)
sock.close
