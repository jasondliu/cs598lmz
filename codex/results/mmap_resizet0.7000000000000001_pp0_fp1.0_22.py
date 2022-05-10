import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This is expected to read back a single zero byte, but it fails with
<code>Traceback (most recent call last):
  File "./test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot read memory at 0x0000000000
</code>
I would expect the memory map to be updated when I truncate the file.
I am using Python 3.4.3 on Debian Jessie.


A:

I'm guessing this is a bug in mmap. I don't think it's doing a <code>fsync</code> after <code>ftruncate</code>.
If you <code>f.flush()</code> before truncating, it works as expected.

