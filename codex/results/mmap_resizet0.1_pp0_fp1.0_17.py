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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap(f.fileno(), 0)</code> to create the memory map. The second argument is the length of the memory map, and you are passing <code>0</code> which means that the length of the memory map is the same as the length of the file.
When you call <code>f.truncate()</code> you are truncating the file to zero length, which means that the memory map is now longer than the file.
You can fix this by passing the length of the file to <code>mmap.mmap</code> instead of <code>0</code>:
<code>m = mmap.mmap(f.fileno(),
