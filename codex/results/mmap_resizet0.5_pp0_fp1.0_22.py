import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I'm not sure why I'm getting this error. It seems like the <code>mmap</code> object is not aware that the file's size has changed. How can I fix this?


A:

You can resize the <code>mmap</code> object using <code>m.resize()</code>, but you also need to resize the underlying file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]

print(a)
</code>

