import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 49
</code>
Or you could save the position of the last <code>0</code>, and then go back and change it to a <code>1</code>.

