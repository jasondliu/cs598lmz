import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(1))
    m.close()
</code>
This gives me the error <code>ValueError: cannot write bytes at read-only memory</code>.
I'm using <code>mmap.mmap(f.fileno(), 0)</code> to map the entire file.
Is there a way to make this work?


A:

I found the problem. I was using python 3.7.0, which is not supported by <code>mmap</code>.

