import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The attribute is only None after the last <code>m[:]</code> line when I run this, even if I comment out the first block opening and writing to the file. So that seems to be the problem: I can't read the file even after closing it if the file has a memory map with the same fd.
The only workaround I've found is creating the mmap with a fixed size, eg. <code>mmap.mmap(f.fileno(), 2)</code>. Is there a way to unblock the file from the mmap?
UPDATE:
The problem is specifically related to <code>MATLAB</code>. When I run the code manually (ie. without a MEX call), the file is unblocked.

