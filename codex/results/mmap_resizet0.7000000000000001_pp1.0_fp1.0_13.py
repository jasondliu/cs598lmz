import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    #m[:] = b'a'
    m.close()
</code>
Which gives the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Is there a solution to this? I'm thinking that I can't truncate a file and then mmap it, but I want to be able to mmap it and then truncate it.

