import select
# Test select.select() call
import select
import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))
s.listen(1)

while True:
    rlist, _, _ = select.select([s], [], [], 0)
    if rlist:
        conn, addr = s.accept()
        print('client connected')
    else:
        print('sleep')
        time.sleep(random.random())

# Run it as many times as you wish.
# The server will accept a client and then sleep for a random
# amount of time.
# It is important that the server is not busy-waiting.
# You can check this by running "top" or "ps" in another window.

# When you are finished, you can kill the server by typing Ctrl-C
# in the server window.
