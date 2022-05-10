import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that this is because <code>truncate</code> doesn't change the file size, but only the end of file.
Is there a way to truncate the file and keep the mmap valid?


A:

You can't do this with <code>mmap</code> alone. You can use <code>os.ftruncate</code> to truncate the file, but you'll need to create a new <code>mmap</code> object to map the new file size.

