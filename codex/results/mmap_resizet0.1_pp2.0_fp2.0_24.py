import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> parameter set to 0.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
This means that the <code>mmap</code> object will be created with a length of 0, and the offset will be set to the current file position, which is 0.
When you then truncate the file, the offset is still 0, but the length is now 0, so the offset is greater than the length.
You can fix this by setting the length to the size of the
