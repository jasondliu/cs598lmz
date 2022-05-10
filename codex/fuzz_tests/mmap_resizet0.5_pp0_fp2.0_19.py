import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that <code>truncate()</code> changes the size of the file and the file pointer is at the end of the file. But, does it mean that the offset of the mmap object is greater than the file size?
I think that the offset of the mmap object is the offset of the file pointer. But, I don't know why the offset of the mmap object is greater than the file size.
I want to know the reason why the offset of the mmap object is greater than the file size.


A:

<blockquote>
<p>I understand that truncate() changes the size of the file and the file pointer is at the end of the file. But, does it mean that the offset of the mmap object is greater than the file size?</p>
</blockquote>
No.
