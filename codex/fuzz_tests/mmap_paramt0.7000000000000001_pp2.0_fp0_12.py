import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(2))
    print(m.read())
</code>
This will print <code>'\x02'</code>, which I believe means that the file was successfully written to.

