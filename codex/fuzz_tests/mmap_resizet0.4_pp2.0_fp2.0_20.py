import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't understand why I'm getting this error. I'm using Python 3.3.3 on Ubuntu 13.10.


A:

You are getting the error because you are trying to read from the memory map after you have truncated the file. 
You should either read from the memory map before truncating the file, or you should create a new memory map after truncating the file.

