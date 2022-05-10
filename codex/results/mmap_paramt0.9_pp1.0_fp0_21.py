import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.flush()
    m.seek(0)
    print(m[0])
</code>
This does not print any value (I have tried using this answer but that happens even without <code>os.fsync()</code> call).
However, calling:
<code>print(f.read()[0])
</code>
prints a value without problems.
My question is: Why mmap behaves like that, and how can I print a value using mmap?

