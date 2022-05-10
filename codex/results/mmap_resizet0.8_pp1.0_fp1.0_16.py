import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print("Exiting")
</code>
The result is:
<code>$ python3 mmap.py
Exiting
</code>

