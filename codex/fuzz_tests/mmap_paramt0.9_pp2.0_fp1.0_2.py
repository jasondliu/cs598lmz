import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print('init:', m[:])
    m[0] = b'2'
    print('after write:', m[:])
    m.close()

with open('test', 'rb') as f:
    print('after close:', f.read())
</code>
Output:
<code>init: b'1'
after write: b'2'
after close: b'2'
</code>

