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
view
import time

def incr(n):
    return n + 1

def compute(a, b, c, d):
    e = incr(a)
    time.sleep(0.2)
    f = incr(b)
    g = incr(c)
    h = incr(d)
    return e + f + g + h

import multiprocessing
multiprocessing.Pool().map_async(compute, [(1, 2, 3, 4), (5, 6, 7, 8)]).wait()
import multiprocessing
pool = multiprocessing.Pool(processes=2)
results = pool.map_async(compute, [(1, 2, 3, 4), (5, 6, 7, 8)])
results.wait()
