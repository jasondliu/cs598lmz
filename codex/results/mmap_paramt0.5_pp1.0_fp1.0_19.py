import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
This prints <code>2</code> as expected.
However, when I change the <code>b</code> to <code>t</code> in <code>'r+b'</code>, I get the error <code>TypeError: an integer is required</code>.
Why is this?

