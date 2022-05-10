from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>3s3si')
s.size
s.pack(b'vj', 6, 0)
s.unpack(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n', (3, 4))

#
# _thread 
#
from _thread import stack_size, start_new_thread, allocate_lock

class Bar:
    def __init__(self):
        self.x = 12
        self.grr = 123

def thread_func():
    b = Bar()
    print(b.x, b.grr)

def test_thread():
    start_new_thread(thread_func, ())

#
# _warnings
#
import warnings

def test_warnings():
    warnings.warn(RuntimeWarning('hello'))

#
# _weakref
#
from _weakref import getweakrefcount, getweakrefs

def test_weakref():
    import sys
    import gc

