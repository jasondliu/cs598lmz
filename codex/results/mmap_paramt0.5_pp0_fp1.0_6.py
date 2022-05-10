import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    print(m.readline())
    m.close()
</code>
This code works fine, but I want to know if it is safe. I am concerned that I am not closing the file properly. I am also not sure if I need to close the mmap object.


A:

You don't need to close the <code>mmap</code> object.  It's closed when it's garbage collected.
If you want to close it explicitly, you can use <code>del</code> to remove the reference to it, or use <code>with</code> to make sure it's closed when the block is exited.
The file is closed when the <code>with</code> block is exited.

