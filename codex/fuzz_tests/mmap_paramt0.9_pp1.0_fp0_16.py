import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    for i in range(len(m)):
        m[i] = b'X'

with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    tr_x = m.translate(chr(10).encode())
    print(m.encode())
    m.close()
with open('ff.txt', 'w') as f:
    f.write('\n')

with open('ff.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    for i in range(4):
        print(m[i])
</code>
but I want the output to be:
<code>X
X
X
\n
</code>
How can I achieve it?


A:

I'm not sure exactly what you're trying to do, but it looks like you want to print out the contents of the file in both formats, both in the stream format, as well as in the ascii/
