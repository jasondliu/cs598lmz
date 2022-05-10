import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import pdb
#pdb.set_trace()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

def list_explain(l):
    for i in xrange(len(l)):
        print "list[", i, "] => ", l[i]
                                  
def find_thread_id(thread):
    for tid, tobj in threading._active.items():
        if tobj is thread:
            return tid
    raise AttributeError("no such thread")

def set_thread_name(name):
    thread_id = find_thread_id(threading.currentThread())
    print "thread_id : ", thread_id
    libc.prctl(15, name, 0, 0, 0)


def dblog(msg):
    print msg
    #f = open("/home/intel/log", "a")
    #f.write(msg + "\n")


class msg_sender(threading.Thread):
    def __init__(self, msg
