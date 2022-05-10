import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This however results in 
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: Cannot read from mmap - it is closed
</code>
Is there a way of obtaining the mmap object after file truncation or should I use the following pattern:
<code>close_on_exit = m.close
del m
f.truncate()
m = mmap.mmap(f.fileno(), 0)
close_on_exit()
</code>


A:

A solution that avoids duplicating code:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m.resize(0)
m = mmap.mmap(f.fileno(), 0)
</code>
The assumption is that the file is empty before the operation.

