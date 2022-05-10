import mmap
# Test mmap.mmap class
data = np.random.rand(16).astype('float32')

# m = mmap.mmap(-1, data.nbytes)
# m.write(data.tobytes())
# m.seek(0)
# m.read_into(np.frombuffer(data, dtype='float32'))

# m.close()

# data
# Test mmap.mmap class
data = np.random.rand(16).astype('float32')

f = open('/tmp/test.bin', 'wb')

m = mmap.mmap(f.fileno(), data.nbytes)
m.write(data.tobytes())
m.seek(0)
m.read_into(np.frombuffer(data, dtype='float32'))

m.close()
f.close()

data

# Test mmap.mmap class
data = np.random.rand(16).astype('float32')

f = open('/tmp/test.bin', 'wb')
