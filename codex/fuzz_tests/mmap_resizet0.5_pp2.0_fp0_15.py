import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
If I comment out the line <code>f.truncate()</code>, it works fine.
I'm trying to figure out why this happens. <code>f.truncate()</code> doesn't shrink the file size until the file is closed. So I thought the <code>mmap</code> object is still valid.
I tried to use <code>os.truncate()</code> and <code>m.resize()</code>, but they raise the same exception.
Is there a way to make the <code>mmap</code> object valid after truncating the file?
And why does the <code>mmap</code> object become invalid?


A:

The docs say:
<blockquote>
<p>Note that when modifying a mmap’d file, the modifications will not be
  visible until the
