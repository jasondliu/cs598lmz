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

# works, but doesn't trigger the bug
gc.collect()

# triggers the bug
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
</code>
And here is the output:
<code>$ python3.8 gc_test.py 
Traceback (most recent call last):
  File "gc_test.py", line 20, in &lt;module&gt;
    gc.collect()
  File "/usr/local/Cellar/python@3.8/3.8.4/Frameworks/Python.framework/Versions/3.8/lib/python3.8/gc.py", line 119, in collect
    return _collect(gen)
  File "/usr/local/Cellar/python@3.8/3.8.4/Frameworks/Python.framework/Versions/3.8/lib/python3.8/gc.py", line 463, in _collect
    for ob in _objs_with_refs(objs):
  File "/usr/local/Cellar/python@
