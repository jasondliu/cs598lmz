import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(12)
</code>
This gives me the error: <code>TypeError: an integer is required (got type bytes)</code>.
I'm wondering how I can go about writing a byte value to the file using mmap.


A:

You can't write <code>bytes</code> to a file using <code>mmap</code>. <code>bytes</code> are immutable, and <code>mmap</code> is backed by memory-mapped files and as such requires mutable objects.
You could have a look at this answer for some explanations on the difference between <code>bytes</code> and <code>bytearray</code>, which is mutable, and should work with <code>mmap</code>.
Regarding your first example, you can't write <code>bytes</code> to a text file.

