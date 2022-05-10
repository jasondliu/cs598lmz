import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The error is:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can see the problem. The file is empty, so the offset is greater than the file size. But what is the best way to get around it?
I can't use <code>mmap.MAP_PRIVATE</code>, since I do need to write to the mmap.
I can't use <code>mmap.resize</code>, since I don't have a reference to the original file size.
What's the best way to get around this?


A:

The documentation is a little bit misleading, but what you need to do is to pass the size of the file as the second argument to <code>mmap.mmap</code>
<blockquote>
<p>mmap.mmap(fileno, length[, tagname[, access[, offset]]])</p>
<p>Map length bytes from the file specified
