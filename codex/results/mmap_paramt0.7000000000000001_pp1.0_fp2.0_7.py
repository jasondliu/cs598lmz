import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print m.read(1)
    m.write(bytes(1))
</code>
I get this output:
<code>1
</code>
But if I change the read to <code>read(2)</code>, I get this output:
<code>Traceback (most recent call last):
  File "mmap.py", line 9, in &lt;module&gt;
    print m.read(2)
ValueError: read byte must be in range(0, 1)
</code>
I would expect the same <code>1</code> to be printed, since the file contains only one byte. Is there any way to read more bytes from the mmap?

