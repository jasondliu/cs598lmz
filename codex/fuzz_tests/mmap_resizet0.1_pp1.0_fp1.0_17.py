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
ValueError: cannot mmap an empty file
</code>
I would expect <code>a</code> to be <code>b''</code>.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are trying to access the <code>mmap</code> object after you truncated the file.
The <code>mmap</code> object is a view of the file, and when you truncate the file, the view is no longer valid.
If you want to truncate the file, you need to do it before you create the <code>mmap</code> object.

