import mmap
# Test mmap.mmap.read()

with open('test_mmap.txt', 'w') as f:
    f.write('0123456789')

with open('test_mmap.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read(5)
    m.read(1)
    m.read(1)
    m.read(1)
    m.read(1)
    m.read(1)

os.remove('test_mmap.txt')
</code>


A:

The problem is that the <code>read</code> method of the <code>mmap</code> object doesn't update the object's internal pointer.  It returns the data, but it doesn't update the pointer.  So, when you call <code>read</code> again, it starts at the beginning of the file again.
You can get the current position of the pointer by calling the <code>tell</code> method of the <code>mmap</code> object.  You can move the pointer by calling the
