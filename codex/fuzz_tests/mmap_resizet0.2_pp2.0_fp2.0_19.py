import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is it possible to truncate a file and keep the mmap object valid?


A:

You can't. The mmap object is tied to the file size.
From the docs:
<blockquote>
<p>The mmap constructor takes parameters for the filename, the length of the mapping, access flags, and, optionally, flags and an offset into the file where the mapping starts. The length parameter must be specified, and must be &gt; 0. If length is larger than the current size of the file, the file is extended to contain length bytes. The file must exist. The access flags are the same as those used by the Unix C function mmap(2), and are documented in your system’s mmap(2) manual page. The flags parameter is optional, and defaults to MAP_SHARED. The offset parameter is also optional, and defaults to 0
