import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\0'
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\0'
ValueError: mmap can't modify a readonly or copy-on-write memory map
</code>
I have seen a few other questions on this error, but they all seem to be related to trying to modify a file after it has been mapped.  I am trying to modify the file while it is still open, so I am not sure why this error is occurring.
I am running python 3.5.2 on Ubuntu 16.04.


A:

You can't modify the file while it's mapped.
From the <code>mmap</code> docs:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems.</p>
<p>On Unix, the underlying mmap(2) system call is used. On Windows, the underlying MapViewOfFile() Win32 API call is used. On
