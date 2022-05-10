import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
    m.close()
</code>
Which yields the error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m[0] = 2
ValueError: byte must be in range(0, 256)
</code>
It looks like the python <code>bytes</code> type only accepts integers in the range <code>[0,255]</code>. How can I then write values outside this range to a file using <code>mmap</code>?


A:

You have to use the <code>memoryview</code> class. It is basically a pointer to a memory area. It allows one to access the elements of the memory area directly without conversion. 
<code>from mmap import mmap

with open('test', 'wb') as f:
    f.write(b'\x01')

with open('test', 'r+b') as f:
    m = mmap(f.fileno(), 0)
    mview = memoryview(m
