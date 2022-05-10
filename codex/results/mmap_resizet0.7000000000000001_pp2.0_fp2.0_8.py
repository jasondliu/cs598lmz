import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I expected <code>a</code> to be <code>b''</code> but instead I get a <code>ValueError</code>:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
Why is that? I don't get it.


A:

You have truncated the file. The underlying file size is zero bytes, but the memory mapping still reflects the original 1-byte allocation.
The <code>mmap.mmap()</code> function allows you to specify a size, but you gave it 0, meaning "map the entire file".
You can force the memory mapping to reflect the new file size with:
<code>m.resize(0)
</code>
after which you can read back <code>b''</code> from the mapping.
The <code>resize()</code> method is a bit odd in that it takes the new size in bytes as an argument, not
