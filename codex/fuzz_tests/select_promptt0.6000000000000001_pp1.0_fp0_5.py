import select
# Test select.select()
print('Starting')
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 16000))
sock.listen(5)
input = [sock]
timeout = 10
while True:
    inputready, outputready, exceptready = select.select(input, [], [], timeout)
    if not inputready:
        print('Time out!')
        break
    else:
        print('Processing')

# Test select.select() with epoll
import select
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 16000))
sock.listen(5)
input = [sock]
timeout = 10
epoll = select.epoll()
epoll.register(sock.fileno(), select.EPOLLIN)

# Read
while True:
    events = epoll.poll(timeout)
    if not events:
        print('Time out
