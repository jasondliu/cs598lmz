import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'3'
    m.close()
</code>
I get an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 5, in &lt;module&gt;
    m[0] = b'3'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Why?


A:

The following works for me:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('3')
    m.close()
</code>
And the result is <code>3</code> stored in the file.

