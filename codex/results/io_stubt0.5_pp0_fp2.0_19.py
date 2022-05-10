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
</code>
Here is my test:
<code>import gc, tracemalloc

gc.collect()
tracemalloc.start()
snap = tracemalloc.take_snapshot()

import test

gc.collect()
snap2 = tracemalloc.take_snapshot()

stats = snap2.compare_to(snap, 'lineno')
for stat in stats[:10]:
    print(stat)
</code>
The output is:
<code>test.py:4: size=10 B, count=1, average=10 B
test.py:2: size=10 B, count=1, average=10 B
test.py:11: size=10 B, count=1, average=10 B
test.py:12: size=10 B, count=1, average=10 B
test.py:13: size=10 B, count=1, average=10 B
test.py:14: size=10 B, count=1, average=10 B
test.py:15: size=10 B, count
