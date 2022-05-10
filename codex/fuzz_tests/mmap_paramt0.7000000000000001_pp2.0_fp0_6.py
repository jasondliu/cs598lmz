import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
This code opens a binary file, writes a byte at offset 0, then reopens the file and uses an mmap object to replace the byte at offset 0 with a different byte. I'm wondering if this is the most efficient way to do this.
More generally, I'm wondering if it's more efficient to use mmap objects to perform operations like this, or to just read/write data to a file. The goal is to do this as efficiently as possible, so any suggestions/comments are appreciated!


A:

From the python docs on mmap.mmap:
<blockquote>
<p>Memory mapping is especially useful for accessing small fragments of large files without reading the entire file into memory.</p>
</blockquote>
So if you want to write one byte to a large file, mmap is probably not the best method. It's there for people that want to read or write large portions of a file without having to worry about temporary memory buffers.
For your use case, writing a single byte, I'd say that mmap is an overkill.
Just use the <code>write</
