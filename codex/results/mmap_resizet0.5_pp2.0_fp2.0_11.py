import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get <code>ValueError: mmap closed or invalid</code> on the last line. How can I close the mmap and still use its content?


A:

The <code>mmap</code> object is not a normal Python object. It's a wrapper for a C library, and the garbage collector doesn't know how to call the right destructor. You need to call <code>close</code> explicitly.

