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
This will print <code>b''</code> on Python 3.5.2 and <code>b'\x01'</code> on Python 3.6.1.
I'm not sure if this is a bug or a feature, but it's definitely a change in behavior.

