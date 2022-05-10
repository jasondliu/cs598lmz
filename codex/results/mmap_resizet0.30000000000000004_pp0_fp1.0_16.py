import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I don't understand why this is happening. If I change the code to:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.seek(0)
    a = m.read()
</code>
Then it works. I don't understand why I have to seek the mmap object to 0. The documentation says that the offset is relative to the start of the file, so why does it matter that the file has been truncated?


A:

The documentation says:
<blockquote>
<p>The offset parameter is the offset into the file where the mapping is to begin
