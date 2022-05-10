import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
This prints out <code>b'\x00'</code> as expected. However, if I change the mode to <code>r+</code> or <code>r+t</code>, the same code will produce <code>b'\x01'</code>. Why is the mode relevant for mmap?


A:

I think that the problem is that when you open the file with the <code>'r+'</code> mode, the file pointer is at the end of the file, and <code>mmap</code> only maps the part of the file that is before the file pointer.  So, when you set the first byte to <code>0</code>, that's not actually changing the file; it's just changing the mapped region of the file.  When you close the file, the <code>mmap</code> is discarded, and the file is written out with the original contents.
If you open the file with <code>'r
