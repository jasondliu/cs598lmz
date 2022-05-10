import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I was sure that <code>a</code> does not contain null bytes, but I was wrong.


A:

I think the problem is that the original file may have been truncated, but the underlying mmap object must still be initialized. As such, when you read from it, you get a snapshot of what is still on the disk, even though the underlying data is no longer present in the file. In this case, the file on disk was 1 byte in size (write 1024 bytes to disk, then truncate the file to 1 byte) and the disk held one byte of data. When you read the mmap, you get that one byte.
I think the answer to the question, "why is this a security risk" depends on how the program deals with the extra bytes. If the program will treat them the same as the original bytes, then the program is working as intended. That requires a complex verification process that can be difficult to get right. Other programs may throw an invalid data exception or similar, which could also be considered a security risk insofar as it's a bug in the program.

