import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
In this example the content of the file is not updated. However, if I change the line <code>m[:] = bytes(2)</code> to <code>m[0] = bytes(2)</code> it works. I want to update the whole array at once.

