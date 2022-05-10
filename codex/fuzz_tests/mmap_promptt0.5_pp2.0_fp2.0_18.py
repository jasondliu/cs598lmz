import mmap
# Test mmap.mmap

# Open a file and map it into memory
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Print the file
print m[:]

# Close the file
m.close()
f.close()
</code>
Output:
<code>$ python test.py
file
</code>
I want to be able to do the same thing, but using a file in memory, rather than a file on disk.


A:

<code>mmap</code> is a system call, and it's not possible to map a file that isn't on disk.

