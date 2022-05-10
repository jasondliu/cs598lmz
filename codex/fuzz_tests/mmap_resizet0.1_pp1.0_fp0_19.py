import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object would be updated to reflect the truncation of the file.
Is there a way to make this work?


A:

The <code>mmap</code> object is not updated to reflect the truncation of the file.
The <code>mmap</code> object is a view of the file at a particular point in time.  The file is truncated, but the <code>mmap</code> object is not.  The <code>mmap</code> object is still a view of the file as it was when the <code>mmap</code> object was created.
The <code>mmap</code> object is not updated to reflect changes to the file.  The <code>mmap</code> object is a view of the file at a particular point in time
