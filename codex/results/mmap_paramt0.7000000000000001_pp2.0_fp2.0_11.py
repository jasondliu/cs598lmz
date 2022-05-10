import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()
</code>
The first print prints <code>b'\x00'</code> (contents of the file), the second and third <code>b''</code> (empty string).
This is a minimal example, but it's basically what I have in my code to read a file. The first time it works, then I start getting empty strings.
I am using Python 3.6.2 on Windows 7.
What am I doing wrong?


A:

This is a known problem with the Windows implementation of <code>mmap</code>. You can read more about it here, but the gist of it is that the second <
