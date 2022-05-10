import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x01'</code>.
I don't understand why <code>m[:]</code> doesn't raise an exception.
I know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I also know that the file is truncated, because if I try to write to the file, I get an exception.
I
