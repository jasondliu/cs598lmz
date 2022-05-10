import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('0')
    m.close()
</code>
После этого в файле будет содержаться символ <code>'0'</code>

