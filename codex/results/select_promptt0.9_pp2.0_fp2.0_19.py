import select
# Test select.select().py
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org',80))
s.send(b'GET / HTTP/1.0\n\n')
fd2 = s.makefile('rb',0)

while 1:
    # select.select(lists,empty list,empty list)
    # lists: is wating for file to be read, file to be written, or an exception has occured.
    #        A file that is ready for the specified operation, select() will return a list of
    #        the filenumbers for that file, so that you can then act on it appropriately.
    #        If a timeout is given and the timeout expires without a file being ready,
    #        three empty lists will be returned.
    rl,wl,xl = select.select([fd2], [], [])
    if rl!=[]:
        # rl is a list of file numbers
        # rl[0] = fd2 = socket
        # fd
