from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)


from timeit import Timer
from functools import partial
def timeit(func, *args, **kwargs):
    try:
        t = Timer(partial(func, *args, **kwargs))
        print(func.__name__, min(t.repeat(3, 1000)))
    except:
        print(func.__name__, 'error')
        

import random
def randomwalk(n):
    x = 0
    y = 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)
    
for i in range
