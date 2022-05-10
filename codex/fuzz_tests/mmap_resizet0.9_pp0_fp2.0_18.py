import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
On Windows as well as linux, <code>a</code> is now <code>b'\x00'</code> instead of <code>b'\x01'</code>. Why does <code>mmap.mmap</code> not detect the truncate operation?


A:

Because truncate only updates the file size according to the OS, the data that you were repeating was only imaginary. 
On Linux, when you open a file (to read or to write), the OS reads your file into the memory, if you open a file to write it will create a copy of the file in the server and will only transfer the changes to the file in the hard disk if you close the file or if you flush the file.
Files are only updated in the hard disk when you close the file.

