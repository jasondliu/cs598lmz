import select
# Test select.select
#
# This is a test of select.select
#
#     select.select(rlist, wlist, xlist[, timeout])
#
# This is a test program
#

import time
import select
import socket

class TestSelect:
    def __init__(self):
        self.count = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', 5555))
        self.server_socket.listen(1)

    def run(self):
        rlist = [self.server_socket]
        wlist = []
        xlist = []
        while True:
            print "Waiting for select"
            rlist, wlist, xlist = select.select(rlist, wlist, xlist)
            print "Done select"
            for sock in rlist:
                if sock == self.server
