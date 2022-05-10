import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'\x00')

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x01'
</code>
I am not sure why this happens. I expect the output to be <code>b'\x00'</code>. I am using Python 3.7.3 on Ubuntu 18.04.3.


A:

<code>write_byte</code> writes the byte at the current position, which is the end of the file.
You can use <code>seek</code> to go back to the beginning of the file:
<code>m.seek(0)
m.write_byte(b'\x00')
</code>

