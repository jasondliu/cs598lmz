import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\x02'
</code>
Note that some OSs may cache file contents in memory. In this case you can use <code>os.fsync()</code> or <code>File.flush()</code> to write it to the disk in the right place (before closing the file).

