import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.seek(0)
    f.write(bytes(2))
    b = m[:]

print('a:', a)
print('b:', b)
</code>
Output:
<code>a: b'\x01'
b: b'\x02'
</code>
as you can see <code>m[:]</code> just before truncate returns <code>1</code>, and <code>m[:]</code> just after truncate returns <code>2</code>.
I thought that <code>m[:]</code> after truncate should return <code>1</code> as well.
Why is this happening?
I'm using Python 3.6.


A:

I'm not too familiar with <code>mmap</code>, but I think the issue is that the <code>m</code> variable is a mutable object representing a memory-mapped file.
The first time you call <code>m[:]</code>, your code reads the first byte of the file and returns it. The second time, your code reads the first byte of the file and
