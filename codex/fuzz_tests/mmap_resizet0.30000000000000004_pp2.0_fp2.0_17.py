import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The code above throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I expected the mmap to be valid.
Is there a way to keep the mmap valid after truncating the file?


A:

The file size is 0, but the mmap size is still 1.  You can't read from the mmap because it's out of bounds.  You can write to it, though.
<code>&gt;&gt;&gt; m.size()
1
&gt;&gt;&gt; m[:]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: mmap offset is greater than file size
&gt;&gt;&gt; m[0] = b'a'
&gt;&gt;&gt
