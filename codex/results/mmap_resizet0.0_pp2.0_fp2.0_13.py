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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> incorrectly.
The first argument is the file descriptor, not the file object.
The second argument is the length of the mapping, not 0.
The third argument is the offset into the file, not 0.
The fourth argument is the access, not 0.
The fifth argument is the tagname, not 0.
The sixth argument is the protection, not 0.
The seventh argument is the flags, not 0.
The eighth argument is the fileno, not 0.
The ninth argument is the length, not 0.
The tenth argument is the offset, not
