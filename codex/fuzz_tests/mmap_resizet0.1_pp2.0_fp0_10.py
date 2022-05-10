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

The problem is that you are using <code>mmap.mmap(f.fileno(), 0)</code> to create the mmap. The second argument is the length of the mapping. If you pass 0, the mapping will be the length of the file.
So, when you truncate the file, the mapping is still the same size as the original file.
You can fix this by passing the length of the file to <code>mmap.mmap</code>.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test',
