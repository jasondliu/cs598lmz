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

# Try to move the buffer to another thread
import threading

def f():
    global view
    view = view[:1]
    threading.get_ident()

t = threading.Thread(target=f)
t.start()
t.join()
del t

# Try to move the foreign object to another thread without having
# a usable thread state
def f():
    global captured
    captured = threading.get_ident()
    threading.get_ident()

t = threading.Thread(target=f)
t.start()
t.join()
del t
