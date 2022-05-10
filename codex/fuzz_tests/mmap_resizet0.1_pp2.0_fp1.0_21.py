import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>f.fileno()</code> to get the file descriptor. This is not a good idea, because it is not guaranteed to be valid after the file is closed.
The solution is to use <code>f.fileno()</code> only once, and then use the file descriptor to create the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    fd = f.fileno()
