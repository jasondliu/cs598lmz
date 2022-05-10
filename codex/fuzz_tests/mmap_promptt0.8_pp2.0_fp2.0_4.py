import mmap
# Test mmap.mmap
# with open("/tmp/test.txt", "w+") as f:
# 	f.write("0123456789")
# 	f.seek(0)
# 	m = mmap.mmap(f.fileno(), 0)
# 	m[0:5] = 'abcde'
# 	m.close()
# 	f.close()

# #Test mmap.ACCESS_READ
# with open("/tmp/test.txt", "w+") as f:
# 	f.write("0123456789")
# 	f.seek(0)
# 	m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# 	print m[0:5]
# 	m.close()
# 	f.close()


# #Test mmap.mmap(..., offset=..., size=...)
# with open("/tmp/test.txt", "w+") as f:
# 	f.write("01234567
