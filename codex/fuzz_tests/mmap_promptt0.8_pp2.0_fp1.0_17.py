import mmap
# Test mmap.mmap() by making a copy of a file.
def backup(filename):
	with open(filename,'r+b') as f:
		with mmap.mmap(f.fileno(),0,access=mmap.ACCESS_COPY) as m:
			with open('bkp.data','w+b') as bkp:
				bkp.write(m)
				print(m[:10])

# Set the entire content of the memory-mapped file
def set_entire(filename,s):
	with open(filename,'w+b') as f:
		f.write(s.encode())
		with mmap.mmap(f.fileno(),len(s)) as m:
			m[:] = s.encode()

# Set the first eight bytes of the memory-mapped file
def set_part(filename,s):
	with open(filename,'w+b') as f:
		f.write(b'abcdefghijklmn')
		with mmap
