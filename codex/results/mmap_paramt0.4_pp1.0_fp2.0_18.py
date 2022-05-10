import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
I get this error:
<code>TypeError: 'bytes' does not support the buffer interface
</code>
I'm using Python 3.3. 
How can I write a byte to a file using mmap?


A:

You can't use <code>bytes</code> objects with mmap.
<code>mmap</code> is a wrapper around the system <code>mmap()</code> function, which lets you map a file into memory and interact with it as if it were an array of bytes.  <code>bytes</code> objects are immutable and don't support the buffer interface, so they can't be used with <code>mmap</code>.
You can use <code>bytearray</code> objects instead.  <code>bytearray</code> objects are mutable and support the buffer interface, so they can be used with <code>mmap</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r
