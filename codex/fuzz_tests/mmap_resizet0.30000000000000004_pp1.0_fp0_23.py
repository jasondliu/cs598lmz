import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I would expect <code>a</code> to be an empty byte string.
Is there a way to achieve this?


A:

The <code>mmap</code> module is not designed to work with empty files.
The documentation for the <code>mmap</code> module states:
<blockquote>
<p>The mmap() function requires a file descriptor fd referring to an open file, a length in bytes, and flags that control the operation of the mapping. The file descriptor fd must be opened with read permission, regardless of whether MAP_PRIVATE or MAP_SHARED is specified in flags.</p>
</blockquote>
The <code>mmap</code> module is designed to map a file into memory.  You cannot map a file into memory if the file is empty.

