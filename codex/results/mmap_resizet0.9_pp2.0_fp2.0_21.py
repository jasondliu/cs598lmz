import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # Reads an empty array.
    m[:] = bytes(1)  # Does not modify the file.
    m.seek(0)
    b = m[:]  # `m` still contains the same data.
    m.flush()
    c = m[:]  # `m` still contains the same data.
    m.close()
    d = m[:]  # `m` closes.

print(a, b, c, d)
# b'' b'' b''
</code>
So to solve your problem, you have some options:
Option A:
<code>with open('db.sl3', 'wb') as f:
    f.write(bytes(1))

with open('db.sl3', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b''
    m.flush()
</code>
Option B:
<code>with open('db.sl3', 'wb') as f:
    f.write(bytes(1))
    m = mmap.
