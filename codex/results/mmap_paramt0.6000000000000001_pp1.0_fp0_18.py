import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
    m.flush()
    m.close()

if os.path.getsize('test') == 0:
    print('empty')

os.unlink('test')
</code>

