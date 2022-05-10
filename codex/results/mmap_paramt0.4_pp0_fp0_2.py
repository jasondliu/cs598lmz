import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.flush()
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = 0
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Why is that?


A:

You are opening the file in read-only mode.
<code>with open('test', 'r+b') as f:
</code>
The <code>r</code> in <code>r+b</code> is the problem. It should be <code>w+b</code>.

