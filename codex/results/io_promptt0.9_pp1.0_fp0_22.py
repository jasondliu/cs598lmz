import io
# Test io.RawIOBase base class
buf = io.BytesIO()
try: buf.write(memoryview(b'abc'))
except TypeError: pass
else: print('SKIP')
buf = io.BytesIO()
try: buf.write(bytearray(b'abc'))
except TypeError: pass
else: print('SKIP')

try: super(io.RawIOBase, 0)
except TypeError: pass
else: print(1)
try: super(io.BytesIO, 0)
except TypeError: print(2)

import io
class MyBytesIO(io.BytesIO):
    def write(self, b):
        return io.BytesIO.write(self, memoryview(b))

b = MyBytesIO()
try:
    b.write(u'abc')
except TypeError:
    print('OK')
else:
    print('Error')

# Check that threads are not preempted from within file I/O methods

import threading, time

def thread_target():
    time.sleep(10)
    print("Error")


