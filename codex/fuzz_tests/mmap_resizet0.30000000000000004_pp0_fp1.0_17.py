import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I am trying to truncate the file, but I am getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    f.truncate()
ValueError: cannot truncate a mmap backing file
</code>
Is there any way to truncate the file?


A:

You can't truncate a file that is mmap'ed.  You can unmap it, truncate it, and then remap it.  The following code works for me:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
</code>

