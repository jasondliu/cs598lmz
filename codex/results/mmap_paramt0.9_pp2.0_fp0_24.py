import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)  # seek to beginning of file
    m[0] = bytes(1)  # change the first byte in file
</code>
The output of this code is:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0] = bytes(1)  # change the first byte in file
TypeError: mmap slice assignment must be a bytes-like object, not 'bytes'
</code>


A:

I found the solution, using <code>b'\xFF'</code> instead of <code>bytes(1)</code>. You can't overwrite this byte, beacause the reference to bytes(1) object was overwritten. Here is the working code with the same output:
<code>import mmap

with open('test.txt', 'wb') as f:
    f.write(bytes(1))

with open('test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
