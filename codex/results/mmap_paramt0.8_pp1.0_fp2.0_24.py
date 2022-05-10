import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.tell())
    m.write(b'foo')
    print(m.tell())
    print(m.tell(), file=f)
</code>
I would expect this to print <code>3</code>, since <code>m.tell()</code> returns the position of the stream, which, as I understand it, would be the position of the stream in the mapped region, which would be 3 after <code>m.write(b'foo')</code>.
However, the <code>print</code> statement prints <code>4</code>, which is the position of the stream in the whole file, not the mapped region.
Why is this?

