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
  File "&lt;stdin&gt;", line 5, in &lt;module&gt;
ValueError: mmap length is zero
</code>
I don't understand why this is happening. I have also tried <code>m.resize()</code> with the same results.


A:

<code>m[:]</code> is trying to read the whole memory mapped file.  It's using the original size of the file to determine the range.  Even though the file is truncated, the memory map is still using the original size of the file.
You can force the memory map to re-size itself by updating the size in the <code>mmap</code> object:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    # Update memory
