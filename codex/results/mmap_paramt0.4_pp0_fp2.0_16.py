import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = bytes(2)
    print(m[0])
    m.close()
</code>
This code prints <code>1</code> and <code>2</code>, which is what I expect. However, when I replace the line <code>print(m[0])</code> with <code>print(m[0:1])</code>, it prints <code>b'\x01'</code> and <code>b'\x02'</code>.
Why is this the case?


A:

<code>m[0]</code> returns an integer, not a byte.
<code>m[0:1]</code> returns a slice, which is a byte.

