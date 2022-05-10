import select
# Test select.select is correct on 0.0.0.0
# test passed in ipv4 only system
# Please run it with python2 as python3 does not show the bug
import socket
import ssl
ssl.wrap_socket(socket.socket(socket.AF_INET)).bind(('0.0.0.0', 0))

# message from Alex Gaynor
leaked = []
def callback(value, tc):
    leaked.append(value)

orig_socket = socket.socket

# class mysocket(socket.socket):
#     def __init__(self, *args, **kwargs):
#         super(mysocket, self).__init__(*args, **kwargs)
# 
#     def accept(self):
#         self.cb(self)
#         return orig_socket.accept(self)

import threading

def start_server(cb):
    sock = socket.socket(socket.AF_INET)

    sock.bind(('', 8888))
    sock.listen(5)
    for i in xrange(2):
        sock.
