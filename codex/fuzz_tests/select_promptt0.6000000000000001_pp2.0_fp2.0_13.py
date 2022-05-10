import select
# Test select.select with a socket.
#
# The socket should be non-blocking, and have a timeout set.
#
# select.select should return 3 lists of objects that are ready.
#
# The first list contains the objects that are readable.
#
# The second list contains the objects that are writable.
#
# The third list contains the objects that had an error.

import socket
import select
import time

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)

s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print 'Connected by', addr

while 1:
    time.sleep(2)
    # select.select([conn], [], [])
    ready_to_read, ready_to_write, in_error = select.select([conn], [], [], 2)
    # print conn
    # print ready_to_read
    # print ready_to_write
   
