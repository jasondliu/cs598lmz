import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This prints <code>b'\x01'</code> on Python 3.5, but <code>b''</code> on Python 3.6.
The behavior seems to be the same on Python 3.7 and 3.8.
Is there a way to make the Python 3.6 behavior consistent with the Python 3.5 behavior?

