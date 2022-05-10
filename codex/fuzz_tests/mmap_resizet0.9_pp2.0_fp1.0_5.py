import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code> Exception ignored in: &lt;mmap.mmap object at 0x7fe8c4882ba0&gt;
 Traceback (most recent call last):
   File "/usr/lib/python3.6/mmap.py", line 145, in _mmap_file_wrapper
     mmap.mmap(self.fileno(), *args)
 OSError: [Errno 9] Bad file descriptor
</code>
It seems that the file descriptor is invalidated when the underlying file is truncated.
Is it possible to continue using the mapped file after truncation? Of course, if I re-map it, the mapped file becomes empty.


A:

Seems like its a known issue: https://bugs.python.org/issue10312

