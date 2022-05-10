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
I don't understand why the mmap offset is greater than the file size. I thought that the mmap offset is the offset from the beginning of the file.
I'm using Python 3.6.3 on Windows 10.


A:

The problem is that you're using <code>f.fileno()</code> to get the file descriptor.  This is a bad idea, because it's not guaranteed to be the same as the file descriptor used by the <code>mmap</code> object.  Instead, you should use <code>m.fileno()</code>.

