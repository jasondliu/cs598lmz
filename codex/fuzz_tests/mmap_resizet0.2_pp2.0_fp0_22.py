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
I would expect that the mmap object would be updated to reflect the truncation.  Is there a way to do this?


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of a file, and the file is truncated. The <code>mmap</code> object is not a view of the file, it is a view of the file's contents.
The file's contents are not truncated. The file's contents are unchanged. The file's contents are the same as they were before the truncation.
The file's contents are the same as they were before the truncation, but the file's size is now zero.
The <code>mmap</code> object is a view of the file's contents, and the file's contents
