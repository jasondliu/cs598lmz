import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>
I'm using python 3.7.3 on MacOS Mojave 10.14.5.
I have also tried <code>f.truncate(0)</code> and <code>f.truncate(1)</code> but the result is the same.

