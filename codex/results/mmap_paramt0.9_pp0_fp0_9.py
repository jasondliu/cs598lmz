import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[4] = bytes(10)

del m
with open('test', 'rb') as f:
    print(f.read())
</code>
Prints:
<code>b'\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>
Though I was expecting the output to be:
<code>b'\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>


A:

Looks like at the moment there isn't a way to do this without adjusting the file size. 
The <code>mmap.mmap</code> constructor returns an instance of <code>_mmap
