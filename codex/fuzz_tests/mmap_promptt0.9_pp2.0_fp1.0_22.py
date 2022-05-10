import mmap
# Test mmap.mmap on a file opened for reading
with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("First 10 bytes via read :", m.read(10))

    # rewind
    m.seek(0)

    print("First 10 bytes via slice:", m[:10])

    print("2nd   10 bytes via read :", m.read(10))

m.close()
</code>
Output:
<code>First 10 bytes via read : b'string of t'
First 10 bytes via slice: b'string of t'
2nd   10 bytes via read : b'ext, part 2'
</code>

EDIT:
Be aware though - <code>mmap</code> is not magic. If you <code>read</code>, <code>write</code> or <code>seek</code> it will keep a current position in the file and change it everytime you read, write, seek etc.
What means, that you can use:
<code>with open("test.txt",
