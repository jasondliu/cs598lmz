import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'2')
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>2</code> but I expected <code>1</code>.
Why am I unable to overwrite the content of the file?


A:

You are opening the file in binary mode, which means that the file offset is always an exact multiple of the underlying block size (usually 512 bytes). So you can't <code>seek</code> to an arbitrary position.
If you open the file in text mode, the file offset is always an exact multiple of the character size (usually 1 byte). So you can't <code>seek</code> to an arbitrary position.
If you open the file in text mode and specify a <code>newline</code> argument, the file offset is always an exact multiple of the newline size (1 byte for <code>'\n'</code>, 2 bytes for <code>'\r\n'</code>). So you can't <code>seek</code> to an arbitrary position.
The only
