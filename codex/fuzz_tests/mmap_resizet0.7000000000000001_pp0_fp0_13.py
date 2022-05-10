import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If I comment out <code>f.truncate</code>, the code runs without error. If I uncomment it, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
My guess is that <code>mmap</code> is holding onto some internal reference to the file that it doesn't account for truncating.
Is there a way to get <code>mmap</code> to work after truncating the file?


A:

You can use <code>m.resize()</code> to resize the mapped region to the new size:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>
<code>m = mmap.mmap(f.fileno(),
