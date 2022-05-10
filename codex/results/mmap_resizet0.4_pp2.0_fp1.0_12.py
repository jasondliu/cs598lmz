import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
and I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there a way to truncate a file and still be able to read the data that was previously there?


A:

The <code>mmap</code> object is tied to the file size.  You can't change the file size and have the mmap object continue to work.
You can truncate the file and then re-open the mmap object with the new size.  But you'll lose the data that was in the original mmap object.

