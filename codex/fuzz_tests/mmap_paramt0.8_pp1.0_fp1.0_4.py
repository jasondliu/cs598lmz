import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m.read())
</code>
Which prints:
<code>b'\x01\x02'
</code>
It's no problem to just buffer read operations though:
<code>def read(self, size=None):
    if size:
        return self.buffer
    else:
        return self.buffer[:size]
</code>

