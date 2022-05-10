import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size has changed, but I don't understand why the <code>mmap</code> object doesn't reflect that.
I'm using Python 3.6.


A:

The problem is that the <code>mmap</code> object is not aware of the file size change.
The documentation says:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. It
  is not supported on systems which do not support the mmap() system
  call (e.g. OS/2).</p>
</blockquote>
The <code>mmap</code> object is a wrapper around the <code>mmap</code> system call.
The <code>mmap</code> system call is documented here:
<blockquote>
<p>The mmap
