import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()
</code>
This gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I thought that by opening the file in read/write mode, I could write to the file. What am I doing wrong?


A:

<code>mmap.mmap</code> objects do not support item assignment.  If you want to write to the file, you need to use the <code>write</code> method.  For example:
<code>m.write(bytes(2))
</code>
or
<code>m.write(b'\x02')  # same as bytes(2)
</code>

