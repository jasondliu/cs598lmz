import sys, threading
threading.Thread(target=lambda:sys.stderr.write('a')).start()

import sys, thread
thread.start_new_thread(lambda:sys.stderr.write('a'), ())

import ctypes
def cfunc_fn(sz):
    sys.stderr.write(ctypes.create_string_buffer(sz).value)

buf = ctypes.create_string_buffer('a')
thread.start_new_thread(cfunc_fn, (buf,))

ctypes.CDLL(None).sz_fnptr(lambda sz: sys.stderr.write(sz))

class GetStderr(object):
    def __call__(self):
        return sys.stderr

GetStderr()()().write('a')

import Queue, thread
q = Queue.Queue(0)
q.put(sys.stderr.write)
thread.start_new_thread(q.get(), ('a',))

@staticmethod
def f():
    sys.stderr.write('a')
