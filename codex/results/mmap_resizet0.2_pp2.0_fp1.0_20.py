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
ValueError: mmap length is zero
</code>
I'm not sure what I'm doing wrong. I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are truncating the file after you have created the mmap. 
<code>m = mmap.mmap(f.fileno(), 0)
f.truncate()
</code>
You need to truncate the file before you create the mmap.
<code>f.truncate()
m = mmap.mmap(f.fileno(), 0)
</code>

