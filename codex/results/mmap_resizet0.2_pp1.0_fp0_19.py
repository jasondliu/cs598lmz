import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the mmap object is now invalid, but I don't understand why. I thought that the mmap object was just a view of the file, and that the file was still there.
I'm using Python 3.6.1 on Windows 10.


A:

The <code>mmap</code> object is a view of the file, but the file is not a view of the <code>mmap</code> object.
The <code>mmap</code> object is a view of the file at the time it was created.  It does not change when the file changes.  If the file changes, the <code>mmap</code> object is no longer valid.

