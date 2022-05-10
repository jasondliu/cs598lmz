import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code works fine on Windows, but on Linux it raises <code>OSError: [Errno 22] Invalid argument</code> on <code>a = m[:]</code>.
How can I make it work on Linux?


A:

I think the problem is that you are trying to read from a file that has been truncated.
<code>f.truncate()</code> truncates the file to 0 bytes.
So when you try to read from the file, it gives you an error.

