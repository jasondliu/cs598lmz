import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I know that I can use <code>m.resize()</code> to resize the mmap, but I don't know how to get the new size of the file.
Is there a way to get the new size of the file after <code>truncate()</code>?

