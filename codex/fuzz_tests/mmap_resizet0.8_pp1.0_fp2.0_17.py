import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
<code>bytes(1)</code> is used to write a single byte to the file. When I simply close the file and open it directly in binary mode, I get the expected result:
<code>with open('test', 'rb') as f:
    a = f.read()
    print(a)
</code>
Output:
<code>b'\x00'  # This is correct
</code>
But when I try to use <code>mmap</code>, I get the following error:
<code>Traceback (most recent call last):
  File "/home/darcy/test.py", line 11, in &lt;module&gt;
    print(a)
OSError: [Errno 104] Connection reset by peer
</code>
I'm using Python 3.8.1
Why does this happen and how can I fix it?

