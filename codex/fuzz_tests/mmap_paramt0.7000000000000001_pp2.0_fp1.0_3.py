import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.flush()
</code>
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m.flush()
ValueError: flush of negative size
</code>
I'm not sure what's going on here.  I can read and modify the file just fine, but I can't flush it.  I know the file is opened in read-write mode.
I'm using Python 3.6.5 on macOS 10.13.3.

