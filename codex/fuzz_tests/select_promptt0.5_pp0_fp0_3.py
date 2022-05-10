import select
# Test select.select() on a socket with a timeout

import socket, time

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to localhost:8080
s.connect(('localhost', 8080))

# send some data
s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')

# wait for a response
timeout = 1.0
start = time.time()
print('Waiting up to %s seconds for a reply' % timeout)
ready = select.select([s], [], [], timeout)
elapsed = (time.time() - start)
print('%s: %s' % (elapsed, ready))
if ready[0]:
    data = s.recv(4096)
    print(repr(data))
else:
    print('no response from server')

# close the connection
s.close()
</code>

