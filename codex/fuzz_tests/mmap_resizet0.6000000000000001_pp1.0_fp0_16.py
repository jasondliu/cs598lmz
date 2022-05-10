import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an <code>OSError</code>:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
OSError: [Errno 22] Invalid argument
</code>
I'm not sure why it raises an exception. I expected the mmap to be empty.


A:

The second argument of <code>mmap</code> is the length. If you pass <code>0</code>, it will try to map the entire file, but since the file is empty, that won't work.

