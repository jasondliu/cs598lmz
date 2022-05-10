import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.seek(0)
    m.write(bytes(1))
</code>
results in:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.write(bytes(1))
OSError: [Errno 22] Invalid argument
</code>


A:

The error is because you are trying to write more bytes than your file contains. As the documentation states, "the <code>write</code> method can only modify bytes in the memory range originally mapped." In this case, you only mapped the single byte <code>0x01</code>, so you can only write a single byte.
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.read(1
