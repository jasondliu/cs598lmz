import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'
    m.close()
</code>
But this gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = b'1'
TypeError: write() argument must be str, not bytes
</code>
I am using python 3.4.3.


A:

<code>mmap</code> is a <code>bytes</code> object, and you index into it with <code>int</code>s. 
<code>m[0] = b'1'
</code>
should be
<code>m[0] = b'1'[0]
</code>

