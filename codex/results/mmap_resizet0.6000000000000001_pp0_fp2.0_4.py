import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # &lt;-- BufferError
</code>
I understand the reason for the exception: the data that was in the buffer, is now invalid.
I wonder if there is a way to force the buffer to be resized, so that it fits the new file size.

