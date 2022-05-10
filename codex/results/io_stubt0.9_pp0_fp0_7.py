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
The test routine is:
<code>&gt;&gt;&gt; stats = []
&gt;&gt;&gt; max = 10000
&gt;&gt;&gt; while len(stats) != max:
...     t = timeit.Timer('f.read(1)', 'from __main__ import f')
...     stats.append(min(t.repeat(10, 100)))
... 
</code>
One might have expected the time to go up as the structure of views grows without bound, but the following plot shows otherwise:

I have repeated this experiment with buffers containing unicode strings, but that only affects the amount of storage needed to contain the views, not the number of views that must be traversed to find the correct buffer.

