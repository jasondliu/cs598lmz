import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]   # line 6
</code>
This raises an exception:
<code>  File "/usr/lib/python3.5/mmap.py", line 24, in __getitem__
    orig_pos = self.tell()
TypeError: invalid argument

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "bug.py", line 10, in &lt;module&gt;
    a = m[:]
  File "/usr/lib/python3.5/mmap.py", line 28, in __getitem__
    tmp = bytes(self[orig_pos : i + 1])
ValueError: Source object of type 'memoryview' is not a bytes-like object
</code>
Why is this happening and what is the correct way of reading everything from mmap?

