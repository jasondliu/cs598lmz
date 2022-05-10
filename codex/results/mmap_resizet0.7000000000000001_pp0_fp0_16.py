import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This fails with:
<code>Traceback (most recent call last):
  File "C:\Users\mth\Desktop\test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I don't think this is normal. If I do
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
</code>
then it succeeds.
Is this a bug? Is it documented somewhere?
I'm using Python 3.5.3 on Windows 10.


A:

I don't think this is a bug.
According to the docs:
<blockquote>
<p>The optional length argument specifies the number of bytes to map. If not specified, the entire file is mapped.</p>
</blockquote>
So when you create the mm
