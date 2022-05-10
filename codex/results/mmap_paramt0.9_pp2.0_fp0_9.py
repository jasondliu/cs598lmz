import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
Documentation says <code>write()</code> from <code>mmap</code> can be used to emulate <code>file.write</code>. However it doesn't seem to work in this example.
Python 3.7

