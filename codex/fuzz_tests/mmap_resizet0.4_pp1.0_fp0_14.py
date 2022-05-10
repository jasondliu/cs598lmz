import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected the output to be <code>b'\x01'</code>, but instead I got <code>b''</code>.
I don't understand why.
I know that if I open the file in append mode, it works, but I don't know why.
I also know that if I open the file in read mode, it doesn't work.
I don't understand why.
I also know that if I open the file in read+write mode, it works.
I don't understand why.
I also know that if I open the file in write mode, it doesn't work.
I don't understand why.
I also know that if I open the file in write+append mode, it doesn't work.
I don't understand why.
I also know that if I open the file in append+read mode, it doesn't work.
I don't understand why.
I also know that if I open the file in read+write+append mode, it works.
I don't understand why.
I also know that if I open the file in write+read+append mode, it works.
I
