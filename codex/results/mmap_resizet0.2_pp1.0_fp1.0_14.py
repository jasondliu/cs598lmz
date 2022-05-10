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
ValueError: cannot mmap an empty file
</code>
I don't understand why I get this error. I thought that the <code>mmap</code> object would be updated when I truncate the file.


A:

You can't mmap an empty file.  You can, however, mmap a file of length 0.  If you want to truncate the file, you need to do it before you mmap it.

