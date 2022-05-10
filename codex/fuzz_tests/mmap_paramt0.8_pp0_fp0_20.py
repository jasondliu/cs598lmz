import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')

with open('test', 'r') as f:
    print(f.read())
</code>
The resulting <code>test</code> file would have the value <code>2</code> instead of the <code>1</code> that I have attempted to write to it.
Edit: I am looking for something that will work on Python 2 as well.


A:

Turns out that I had to add a newline to the end of the string. I don't know why, but it worked.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')
    m[1] = ord('\n')

with open('test', 'r') as f:
    print(f.read())
</code>

