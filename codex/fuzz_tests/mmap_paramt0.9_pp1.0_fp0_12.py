import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
This produces no output.
However, the following produces "2":
<code>with open('test', 'r+b') as f:
    print(f.read())
    f.seek(0)
    f.write(bytes(2))
</code>
Does mmap refreshes the read buffer, while f.write() does not?\
In other words, in the first example the f.write() overwrites the byte which was read by mmap?


A:

No.
From the mmap documentation:
<blockquote>
<p>The optional flags argument specifies how the file is to be opened: os.O_RDONLY opens the file for reading only. os.O_RDWR opens the file for reading and writing. If this flag is not specified, it defaults to os.O_RDONLY. <strong>On Unix, if this flag is specified, the file is opened for read and write. To acquire an exclusive lock on the file, O_EXCL should be set in flags and the file created by opening path in the exclusive mode.</
