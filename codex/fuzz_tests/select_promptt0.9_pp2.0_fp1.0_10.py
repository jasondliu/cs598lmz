import select
# Test select.select and select.poll models

import os
import threading
import select
import sys

def server(serv, num_children):
    children = []
    for i in range(num_children):
        pid = os.fork()
        if pid == 0:
            child(_evt=threading.Event())
        else:
            children.append(pid)
    for pid in children:
        try:
            os.waitpid(pid, 0)
        except OSError:
            pass


def child(serv=None, _evt=None):
    sys.stderr.write("child started %d\n" % os.getpid())
    sys.stderr.flush()
    _evt.set()
    conn, addr = serv.accept()
    msg = conn.recv(100)
    conn.close()

def poll(serv, num_children):
    poller = select.poll()
    poller.register(serv, select.POLLIN)
    children = {}
    for i in range(num_children):
        pid
