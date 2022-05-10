import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I was expecting <code>a</code> to be an empty byte array, but instead it is <code>b'\x01'</code>. Why is this?


A:

The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>The optional <em>length</em> argument specifies the size of the mapped region. If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is omitted, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So, when you create the <code>mmap</code> object, you are asking to map the entire file, which is 1 byte long.  Then you truncate the file to 0 bytes.  The <code>mmap</code> object still thinks the file is 1 byte long, so when you try to read it, you get the 1 byte that used
