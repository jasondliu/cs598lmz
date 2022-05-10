import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
OSError: [Errno 22] Invalid argument
</code>
I expected <code>a</code> to be an empty <code>bytes</code> object.


A:

The problem is that you are truncating the file after mapping it. From the documentation
<blockquote>
<p>The file size cannot be changed, and mmap fails if the file is too small.</p>
</blockquote>
So, if you change the order of your operations, it will work:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
</code>

