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
This code will print <code>b'\x01'</code>, and I expected it to raise <code>ValueError</code>.
Why does <code>mmap</code> allow the file to be truncated after the map was created?

