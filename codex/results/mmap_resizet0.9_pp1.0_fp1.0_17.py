import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print('hello')
    b = m[:]
</code>
This gives the following error:
<code>hello
Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'd expected both a and b to be equivalent and empty.  Is there any way to achieve the expected result?
An alternate output would be <code>AttributeError: '_mmap.mmap' object has no attribute '__getitem__'</code> which is slightly less unexpected.
This is Python 3.5.1 on Linux (Debian 8, if it matters).


A:

A <code>mmap</code> is created from an existing file as a view of a region of the file.  Truncating the file does not destroy that view.  Instead, it creates a range of bytes that doesn't exist.  The <code>mmap</code> is still valid and still in use, but those bytes don't exist.  Therefore, if the <code>offset
