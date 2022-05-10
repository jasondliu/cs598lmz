import mmap
# Test mmap.mmap
with open('lorem.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # m = mmap.mmap(f.fileno(), 0)
print('First 10 bytes via read :', m.read(10))
print('First 10 bytes via slice:', m[:10])
print('2nd   10 bytes via read :', m.read(10))

# Explain the difference between read and slice
m.seek(0)
print('First 10 bytes via read :', m.read(10))
print('First 10 bytes via slice:', m[:10])
# Explain the difference between read and slice
m.seek(0)
print('First 10 bytes via read :', m.read(10))
print('First 10 bytes via slice:', m[:10])
m.seek(0)
print('First 10 bytes via read :', m.read(10))
print('First 10 bytes via slice:', m[:10])
