import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
I expected <code>a</code> to be empty, but instead it is <code>b'\x01'</code>.
<code>m[:]</code> is <code>b'\x01'</code> before the <code>f.truncate()</code> call.
Truncating the file before creating the mmap object or opening the file with <code>os.O_TRUNC</code> both work as expected.
I'm on macOS 10.15.5 (19F101) with Python 3.8.5.


A:

It's because you truncate the file and then create the mmap object.
You should create the mmap object first then truncate the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
The mmap object has a size of 1 and
