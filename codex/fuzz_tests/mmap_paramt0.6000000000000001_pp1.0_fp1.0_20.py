import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 49
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I have to use <code>0</code> as the length of the file to map the whole thing, but if I use <code>1</code> or any other value less than the length of the file, the value written is not preserved.
Why is that?


A:

<code>mmap</code> isn't magic, it's just an efficient way of reading and writing files.  If you ask to map a file with a length of 1, you get the first byte of the file.  If you change that byte, and then close the <code>mmap</code>, the file is updated with that change.  But the <code>mmap</code> doesn't know that the file is larger than 1 byte, so if you try to write to the second byte, you get an <code>IndexError</code>.

