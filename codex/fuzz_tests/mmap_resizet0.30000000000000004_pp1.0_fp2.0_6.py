import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I think it is because the file size is 0 after truncate, but the offset of mmap is still 1.
Is there a way to truncate the file and make the mmap object still valid?


A:

You can use the <code>resize()</code> method to resize the mapping:
<code>m.resize(0)
</code>
This will resize the mapping to 0 bytes, and the offset is now 0.

