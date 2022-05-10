import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The result is <code>a</code> is <code>b''</code> instead of <code>b'\x01'</code>.
Is there any way to make the <code>mmap</code> object aware of the file truncation?
(I know I can use <code>m.resize()</code> instead of <code>truncate()</code>, but I want to make the <code>mmap</code> object aware of the file truncation.)


A:

I'm not sure that this is the best solution, but it worked in my test.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]

print(a)
</code>

