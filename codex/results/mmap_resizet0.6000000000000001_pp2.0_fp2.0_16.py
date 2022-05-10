import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This prints <code>b'\x00'</code>.
If you want to truncate to a certain length, instead of to the end of the file, use <code>m.resize</code>.

