import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(1)
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = bytes(1)
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Why is this? Is there a way to make it work?


A:

You can use <code>mmap.resize</code> to grow the size of the file:
<code>&gt;&gt;&gt; m.resize(2)
&gt;&gt;&gt; m[0] = bytes(1)
&gt;&gt;&gt; m.flush()
</code>
Note that you need to call <code>flush</code> to make sure the changes are written to the file.

