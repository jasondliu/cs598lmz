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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I thought that the mmap object would be aware of the truncation. 
Is there a way to get the mmap object to be aware of the truncation?


A:

The <code>mmap</code> object is not aware of the truncation because it is not aware of the file at all.  It is a view into the file, but it is not the file.  It is a view into the file at the time it was created.  The file can change, but the <code>mmap</code> object will not change.
You can create a new <code>mmap</code> object after truncating the file.  You can also use <code>mmap.resize</code> to resize the <code>mmap</code> object.

