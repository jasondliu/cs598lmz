import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows, but on Linux it throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
mmap.error: [Errno 9] Bad file descriptor
</code>
I've tried to use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)</code> instead of <code>mmap.mmap(f.fileno(), 0)</code>, but it doesn't help.
Is there any way to fix this?


A:

You can't use <code>mmap</code> on a file that has been truncated.  The <code>mmap</code> object is still pointing to the old file contents, and the file descriptor is no longer valid.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object, but that won't work if you're trying to shrink the file.

