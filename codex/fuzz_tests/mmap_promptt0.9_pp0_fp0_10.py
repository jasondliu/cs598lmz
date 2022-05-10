import mmap
# Test mmap.mmap.file_size bug.  First, we'll create a file of length
# zero.

with open("f1", "w") as f1:
	pass

try:
	m = mmap.mmap(f1.fileno(), 0, mmap.MAP_SHARED)

	# Check it's really as big as it claims.
	f1.write(' ')
	f1.flush()
	m.flush()

	for i in range(m.file_size()):
		if m[i] != ' ':
			raise TestFailed('expected space in mmap file')
	m.close()
	f1.close()
	os.remove("f1")
except TestFailed as msg:
	print(msg)
