import select
# Test select.select() with large buffersize
# Note that this test fails if select() does not support large buffers

import subprocess
import threading
import time

import _testcapi

def start_server(server_socket):
    # Common code for server processes
    def read_all(sock):
        data = ''
        while True:
            try:
                chunk = sock.recv(1024)
                if not chunk:
                    break
                data += chunk
            except socket.error, e:
                if e.args[0] == errno.EINTR:
                    continue
                raise
        return data

    s, addr = server_socket.accept()
    bufsize = _testcapi.get_largetext()
    # Receive all data from client
    data = read_all(s)
    # Send back data in chunks of bufsize
    for i in xrange(len(data) // bufsize):
        s.send(data[i*bufsize:(i+1)*bufsize])
    s.close()

def start_client(client_socket, data
