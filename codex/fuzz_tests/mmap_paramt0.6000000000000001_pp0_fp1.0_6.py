import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'abc')
    m.seek(0)
    print(m.read(1))  # prints '\x00'

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m.read(1))  # prints '\x00'
</code>
I have a file with 1 byte content. I open it with <code>mmap.ACCESS_WRITE</code> and write 3 bytes. Then I seek back to the beginning and read 1 byte. I expect that byte to be <code>\x00</code> but it is not. It is <code>\x61</code>. I.e. it is the first byte of the string I wrote.
If I open it again with <code>mmap.ACCESS_WRITE</code> and read 1 byte it is <code>\x00</code> as expected.
Why is this?


A:

You
