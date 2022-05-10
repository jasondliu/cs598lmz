import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I thought that the mmap would be updated to reflect the truncation.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

The problem is that you're opening the file in read-only mode.
<code>with open('test', 'r+b') as f:
</code>
The <code>+</code> means that you want to open the file for both reading and writing, but the <code>r</code> means that you want to open it in read-only mode.
If you want to open the file for writing, you need to use <code>w</code> instead of <code>r</code>.
<code>with open('test', 'w+b') as f:
</code>

