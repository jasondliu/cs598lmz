import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This produces the following error:
<code>Traceback (most recent call last):
  File "/home/user/test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
What is the correct way to truncate a file with an open memory map?


A:

The correct way to do this is to use <code>mmap.resize()</code>. You can find the documentation here.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
</code>

