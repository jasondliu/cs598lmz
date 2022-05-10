import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'\x00')

with open('test', 'rb') as f:
    print(f.read())
</code>
My code gives me the following output:
<code>b'\x00\x00\x00'
</code>
But I expected:
<code>b'\x00'
</code>
Anyone know what I'm doing wrong?


A:

You're doing nothing wrong. <code>mmap</code> can't truncate the file. It's just a memory-mapped view of the file. You can't use it to write a shorter file. If you want to write a shorter file, you have to do it the same way you did the first time: with <code>open</code> and <code>write</code>.

