import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using python 3.6.2 on Windows 10.
I am trying to use mmap to read a file that is being written to by another process. I want to be able to read the file while it is being written to.
I am trying to use mmap to read a file that is being written to by another process. I want to be able to read the file while it is being written to.


A:

The problem is that you are truncating the file after you have created the mmap.
You need to truncate the file before you create the mmap.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
   
