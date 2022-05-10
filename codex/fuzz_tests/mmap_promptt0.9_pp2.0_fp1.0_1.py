import mmap
# Test mmap.mmap(NULL)
f = os.open("/dev/zero", os.O_RDONLY)
m = mmap.mmap(f, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ)

# Test mmap.mmap(-1,xx)
try:
	f = os.open("/dev/zero", os.O_RDONLY)
	m = mmap.mmap(f, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ, mmap.MAP_FIXED)
except Exception as e:
	print (e)
finally:
	try:
		os.close(f)
	except:
		pass

try:
	f = os.open("/dev/zero", os.O_RDONLY)
	m = mmap.mmap(f, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ, mmap.MAP_FIXED, -1);
except Exception as e:
