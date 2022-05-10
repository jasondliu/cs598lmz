import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
produces this error:
<code>Traceback (most recent call last):
  File "read_mmap.py", line 7, in &lt;module&gt;
    a = m[:]
ValueError: cannot resize a mapped view
</code>
The documentation does not mention this problem.
I am using Python 3.2.2 on 32-bit Windows 7.

EDIT:
I tried this with Python 2.7.1 (on 64-bit Windows 7), and it works. So at least it's not a Windows thing.


A:

I think the problem is that <code>truncate()</code> doesn't change the size of the underlying file until you flush the file.  Your <code>f</code> is still open, so the file is still not flushed.  You can force a flush by doing
<code>f.flush()
f.truncate()
</code>
Now the file will be truncated, and the file size will be 0 bytes.  So now any attempt to read from <code>m</code> will fail, because
