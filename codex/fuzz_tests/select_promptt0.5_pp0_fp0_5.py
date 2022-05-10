import select
# Test select.select() with a pipe and a socket.
import socket
import sys
import time

def make_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    conn, addr = s.accept()
    return conn

def test():
    conn = make_connection()
    r, w = os.pipe()
    inputs = [r, conn]
    outputs = []
    while 1:
        print "selecting"
        rlist, wlist, xlist = select.select(inputs, outputs, inputs)
        print "rlist = %s" % rlist
        print "wlist = %s" % wlist
        print "xlist = %s" % xlist
        if rlist:
            data = os.read(rlist[0], 1)
            if not data:
                break
            print "read %s from %s" % (repr(data), rlist[0])
            if rlist[0] is r:
