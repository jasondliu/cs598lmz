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
The first argument to <code>mmap.mmap</code> is the file descriptor, not the file object.
The second argument is the length of the mapping.
The third argument is the offset into the file.
The fourth argument is the access mode.
The fifth argument is the tag name.
The sixth argument is the tag value.
The seventh argument is the protection mode.
The eighth argument is the visibility flag.
The ninth argument is the maximum length.
The tenth argument is the flags.
The eleventh argument is the file descriptor
