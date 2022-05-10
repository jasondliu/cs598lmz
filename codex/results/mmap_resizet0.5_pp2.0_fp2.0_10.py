import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # this is where the exception is raised
</code>
The exception is:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is now 0 bytes, and that the mmap offset is 0 bytes. But it doesn't make sense to me that the file size is 0 bytes, since the file is open.
I'm on Windows 7, but I don't think that's relevant.
Is this a bug?
Edit: Maybe this is a bug in the mmap implementation in the Python standard library. I tried the same thing with the mmap module in the pypy standard library, and it worked fine.

