import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
I don't understand why this happens. I thought that the <code>mmap</code> object would be closed when the <code>with</code> block ends.
If I add <code>m.close()</code> to the end of the <code>with</code> block, it works.
I'm using Python 3.5.2.


A:

The <code>with</code> statement is not a context manager for the <code>mmap</code> object. It is a context manager for the file object. The <code>mmap</code> object is closed when the <code>with</code> block ends because it is a local variable in the <code>with</code> block.

