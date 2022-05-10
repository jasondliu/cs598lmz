import select
# Test select.select()

import select
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(5)

print 'Listening on port', s.getsockname()[1]

while True:
    r, w, e = select.select([s], [], [], 1)
    if s in r:
        client, addr = s.accept()
        print 'Got connection from', addr
        client.send('Thank you for connecting')
        client.close()
    else:
        print 'Waiting for connection...'
    time.sleep(1)
