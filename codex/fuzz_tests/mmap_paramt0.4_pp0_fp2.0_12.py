import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.close()
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
ValueError: mmap can't modify a readonly memory map
</code>
I've tried opening the file with <code>'r+b'</code> and <code>'rb+'</code> but neither works.
I'm using Python 3.5.2 on OS X.


A:

The problem is that you open the file in <code>'r+b'</code> mode, which is read-write binary mode. The <code>'r'</code> part means that the file is opened in read-only mode.
You need to open the file in <code>'rb+'</code> mode, which is read-write binary mode. The <code>'b'</code> part means that the file is opened in binary mode.

