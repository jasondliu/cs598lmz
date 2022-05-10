import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
gives:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I am curious why this occurs, as the documentation for <code>mmap.mmap()</code> (Python 3.5.2) states that if the <code>length</code> argument is 0, then the entire file is mapped.
According to the documentation for <code>mmap.mmap()</code> (Python 3.5.2), the <code>length</code> parameter defaults to the current file size, which should be 0. However, <code>m[:]</code> says that <code>m</code> is closed or invalid? I am unsure if this is because the length is 0, or because the file has been truncated.


A:

The problem is that you did not specify the desired <code>length</code> to <code>mmap</code>. The default length is the current size of the file.
