import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'
    m.close()
</code>
I'm trying to change the first byte of the file to <code>1</code> instead of <code>0</code>.
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'1'
TypeError: 'mmap.mmap' object does not support item assignment
</code>


A:

You can't change the size of a file with <code>mmap</code>.
You need to either <code>resize</code> the file first, or create the file with the correct size.
<code>with open('test', 'r+b') as f:
    f.truncate(1)
    m = mmap.mmap(f.fileno(), 1)
    m[0] = b'1'
    m.close()
</code>

