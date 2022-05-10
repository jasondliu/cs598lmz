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
I'm using Python 3.6.3.
Is there a way to get the data from the mmap object after truncating the file?


A:

You can't do this. The mmap object is tied to the file, and the file is truncated.
You can use the <code>mmap.resize</code> method to resize the mmap object, but that will not resize the file.

