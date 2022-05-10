import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

    # read and change content
    mread = m[:]

    mread[0] = b'3'

    m.close()
</code>
gives
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    mread[0] = b'4'
TypeError: an integer is required
</code>
What am I doing wrong? I also attempted to write a byte or a string directly, to no avail (different exception).


A:

The <code>mmap</code> returned by <code>mmap.mmap()</code> is not a bytes-like sequence, it's a binary buffer.
Try 
<code>mread = bytes(m)
</code>
or just
<code>mread = m.read(m.size())
</code>
or
<code>mread = m.read_byte(m.size())
</code>
to read the whole file.
You're also opening the file in
