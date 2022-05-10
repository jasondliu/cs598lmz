import mmap
# Test mmap.mmap(fileno, length)
print('mmap.mmap(fileno, length)')
length = os.path.getsize(file_path)
with open(file_path, 'rb') as f:
    fileno = f.fileno()
    m = mmap.mmap(fileno, length)
    print('mmap.size() %d' % m.size())

# Test mmap.mmap(fileno, length, access)
print('mmap.mmap(fileno, length, access)')
length = os.path.getsize(file_path)
with open(file_path, 'rb') as f:
    fileno = f.fileno()
    m = mmap.mmap(fileno, length, mmap.ACCESS_READ)
    print('mmap.size() %d' % m.size())
    m.close()

# Test mmap.mmap(fileno, length, access, flags)
print('mmap.mmap(fileno, length, access, flags)')
length = os.path.gets
