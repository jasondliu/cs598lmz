import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\0')
</code>
Now, <code>m</code> has length 1 and we tried to write the integer 0 to it (which is translated to bytes <code>\x00</code>). This results in a segfault:
<code>Exception ignored in: &lt;bound method mmap.__del__ of &lt;mmap.mmap size=1&gt;&gt;
Traceback (most recent call last):
  File "/usr/lib64/python3.6/mmap.py", line 284, in __del__
  File "/usr/lib64/python3.6/mmap.py", line 283, in __exit__
  File "/usr/lib64/python3.6/mmap.py", line 237, in close
TypeError: an integer is required (got type bytes)
</code>
I expected that either <code>mmap</code> would not allow a write at size zero (giving <code>ValueError: memory view cannot include element 0</code>) OR that zero would be written (giving an empty file). I
