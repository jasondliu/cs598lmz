import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    a = m[:2]
    a = m[2:]
    a = m[3:]
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm wondering why <code>a = m[:2]</code> and <code>a = m[2:]</code> are legal, which means that our <code>mmap</code>'s length is more than 0 after we truncate the file, but <code>a = m[:]</code> and <code>a = m[3:]</code> will cause errors? Could anyone please provide some advice? Thanks!


A:

The error says that <code>m[:]</code> failed because of the file size. I would think that a mmap longer than the file it's mapped from would throw an error as well, though can understand that it might not be immediately clear how long the mmap is.

