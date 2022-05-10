import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])  # -1
</code>
When <code>mmap</code> is used with <code>ACCESS_COPY</code>, the memory is copied, and any changes made to the copy will not be reflected in the original file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    print(m[0])  # 0
    m[0] = 255
    print(m[0])  # 255

with open('test', 'rb') as f:
    print(f.read()[0])  # 0
</code>
To modify the file in place, use <code>ACCESS_WRITE</code> instead.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('
