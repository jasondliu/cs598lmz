import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code first writes a single byte to <code>test</code> and then creates an mmaped view on this file. Note that the view's size is zero (second parameter to <code>mmap</code>). Then the file is truncated and the mmaped view is read.
If the mmaped view is empty, shouldn't the <code>m[:]</code> line throw an exception? Instead, it returns nothing:
<code>&gt;&gt;&gt; a
b''
&gt;&gt;&gt; len(a)
0
</code>
On the other hand, if I try to read a byte from the mmaped view, it throws an exception:
<code>&gt;&gt;&gt; m[0]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "mmap.py", line 485, in __getitem__
    raise ValueError("mmap offset is greater than file size")
ValueError: mmap offset is greater than file size

