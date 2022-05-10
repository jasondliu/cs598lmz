import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Traceback
<code>Traceback (most recent call last):
  File "c:\Python27\test.py", line 13, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to change the file while still having an access to the whole file through <code>mmap</code>.
How to do that? 
PS. Is it possible with an in-memory-only file?


A:

The problem with your code is that after <code>truncate()</code> the file is empty so that <code>m[:]</code> is invalid.  It will work with some other tricks though, try this:
<code>with open('test', 'wb') as f:
    f.write(b'testfile')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)   

    print(m.read())
    print(f.read())

    f.seek(0)
   
