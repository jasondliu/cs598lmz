import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This code should print <code>b'\x01'</code> but instead it prints <code>b''</code>.
I am using Windows 10, Python 3.6.5, and mmap 0.5.4.


A:

The problem is that you are using <code>truncate()</code> on the file object, which truncates it to the current position of the file pointer.  You should instead use <code>truncate(0)</code> or <code>truncate(1)</code> to truncate to a specific size.

