import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    f.close()
</code>
result:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: memory mapped size must be positive
</code>
I expected <code>a</code> to be empty <code>b''</code>, but there is an exception.


A:

The problem is that you first use the <code>m</code> to get a byte and then you do <code>m.close()</code>.
So you leave <code>m</code> opened in memory and you can't use <code>m</code> in the <code>[]</code> operation.
You can use <code>m.closed</code> to check if the mmap is closed or not.
If you don't close the mmap, you'll get the following error:
<code>OSError: [Errno 9] Bad file descriptor
</code>
Note that you cannot use <code>with</code> statement with <code>mmap
