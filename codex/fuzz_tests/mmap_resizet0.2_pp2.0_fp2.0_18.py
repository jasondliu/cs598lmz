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
ValueError: mmap length is zero
</code>
I would expect <code>a</code> to be <code>b''</code> or <code>[]</code> or something similar.
Why does this happen?


A:

The <code>mmap</code> object is not aware that the file has been truncated.  The <code>mmap</code> object is created with a length of 1, and that length is not changed by the <code>truncate</code> call.  The <code>mmap</code> object is not aware of the file's contents, and it is not aware of the file's size.
The <code>mmap</code> object is a memory-mapped view of the file, not a view of the file's contents.  The <code>mmap</code> object is a view of
