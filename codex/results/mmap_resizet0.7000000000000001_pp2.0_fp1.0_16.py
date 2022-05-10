import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints <code>b'\x00'</code> on Windows, but <code>b'\x01'</code> on Linux. This is because <code>mmap.mmap</code> on Windows only uses the file size at the time the <code>mmap</code> is created. On Linux, the <code>mmap</code> is tied to the file and will grow and shrink with the file. This means that on Windows, the <code>mmap</code> is still valid even though the file is empty, but on Linux, it is not valid.

