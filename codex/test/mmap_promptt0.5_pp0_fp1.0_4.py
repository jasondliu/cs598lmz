import mmap
# Test mmap.mmap on a file

# Open file and read in the whole thing
f = open('/etc/passwd','r')
content = f.read()
f.close()

# Open file and read in the whole thing using mmap
f = open('/etc/passwd','r')
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
m_content = m.read()
f.close()

# Compare contents
