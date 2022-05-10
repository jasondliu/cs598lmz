import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # This raises an error
</code>
Running this code snippet raises the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap can't resize a readonly or copy-on-write mmap
</code>
Why is this happening? I am under the impression the the <code>mmap</code> object should be able to handle the file being resized.


A:

You can find out what's going on by looking at the implementation of <code>mmap.mmap()</code> (source here).
The problem is that <code>mmap()</code> is doing a <code>os.stat()</code> call to determine the size of the file and then doing a <code>os.mmap()</code> call to map that size. But the <code>os.stat()</code> call happens before you do your <code>f.truncate()</code> call, so <code>os.mmap()</code> is mapping the old
