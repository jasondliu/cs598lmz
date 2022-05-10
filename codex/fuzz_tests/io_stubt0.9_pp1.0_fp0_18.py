import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del view
gc.collect()

# Compile a function using bare _PyObject_GenericSetAttrWithDict().
# It can be free'ed at shutdown.
def f(x):
    x.attr = 10
compile(f.__code__, "<test>", "exec")

gc.collect()
gc.collect()

# At shutdown, every thread must have been completely uninitialized.
# In the bug scenario, at least one thread must still be alive
# (otherwise, the bug may not be triggered).
import threading
thread = threading.Thread()
thread.start()
gc.collect()
gc.collect()
del thread
