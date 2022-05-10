import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand why this happens, but I would like to know if it is possible to avoid this error without closing the file. The reason I need to do this is that I am using the file as a buffer for a process and I want to keep the file open while the process is running. I can't close the file because I need to read from it while the process is running.
I tried using <code>mmap.resize</code> but that doesn't work either.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>
This raises an error:
<code>Traceback (most recent call last):
  File "test.py", line
