import mmap
# Test mmap.mmap()
# Test mmap.read(), mmap.write()
# Test mmap.tell(), mmap.seek()
# Test mmap.size()
# Test mmap.close()

# TODO:
# Test mmap.find()
# Test mmap.rfind()
# Test mmap.flush(), mmap.sync()

def test(file_name, num_bytes):
	f = open(file_name, 'r+b')
	m = mmap.mmap(f.fileno(), num_bytes)

	m.write(b'x' * num_bytes)
	m.seek(0)
	assert m.read(num_bytes) == b'x' * num_bytes

	m.seek(0)
	assert len(m.read(num_bytes)) == num_bytes

	assert m.tell() == num_bytes
	m.seek(0)
	assert m.tell() == 0
	m.close()
	f.close()

def test_size(file_name, num_bytes):
	f = open(
