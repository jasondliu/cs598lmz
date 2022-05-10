import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    os.unlink('test')
    m.write(bytes(1))
</code>
The error message is:
<code>Traceback (most recent call last):
  File "m.py", line 8, in &lt;module&gt;
    m.write(bytes(1))
ValueError: mmap closed or invalid
</code>
The goal is to make a memory mapped file in read/write mode, read from it and write to it, and then removing the file. 
Is it possible to do this?
The reason I want to do this is to make a in-memory database for big data. The database itself is not big, but the data in the database is big. If the database file is memory mapped, then it can be read/written without actually loading the database file.

