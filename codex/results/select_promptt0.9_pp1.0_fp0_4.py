import select
# Test select.select
# select_test.py
import time, sys
from socket import *
from select import select
# set up sockets for accept()ing connections
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 18000))
s.listen(5)
s.setblocking(0)
s.settimeout(5) # this will be the idle timeout value for the
# SocketSelect class
# set up the reading list
input = [ s ]
# set up the output list
output = []
# set up the exception list
exception = []
# the "forever" loop
while True:
    # set up the idle timeout value
    # (compute so it ends when the next
    # SS_ACCEPT socket becomes ready)
    timeout = 0.0
    for ss in input:
        if ss is s:
            try:
                r, w, x = select(input, output, exception, timeout)
                # if the socket is ready,
                # go ahead and accept
                if s in r:
