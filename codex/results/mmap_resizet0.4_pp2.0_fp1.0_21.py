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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the error is due to the fact that the file has been truncated and the mmap object is still pointing to the original position. Is there a way to make the mmap object point to the beginning of the file?


A:

<code>mmap</code> objects are not dynamic. They are fixed to a particular region of the file.
You can use <code>mmap.resize()</code> to change the length of the file, but it cannot grow the file.
You can use <code>mmap.remap()</code> to change the file and the region within the file that the <code>mmap</code> object is mapped to.

