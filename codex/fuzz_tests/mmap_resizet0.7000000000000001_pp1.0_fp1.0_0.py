import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # Segmentation fault
</code>
Is there any way to handle this situation without reading all the mmap data before truncation?


A:

Segfault is not the only problem.
<code>$ python3 -mtrace --trace test.py
Traceback (most recent call last):
  File "/usr/lib/python3.7/trace.py", line 25, in _runscript
    sys.settrace(None)
AttributeError: 'NoneType' object has no attribute 'settrace'
</code>
This is a bug in CPython.
A simple workaround is to remove <code>m</code> before <code>f.truncate()</code>.

