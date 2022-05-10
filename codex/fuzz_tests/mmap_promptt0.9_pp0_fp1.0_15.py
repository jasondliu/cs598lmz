import mmap
# Test mmap.mmap()
fp = open('D:\\Tools\\Pytest\\testdata.txt', 'r+')
fp.write('0123456789abcdef')
fp.seek(0)
m = mmap.mmap(fp.fileno(), 15)
print repr(m[0:10])
print repr(m[10:15])

# Test readline()
m.seek(0)
print m.readline()

# Test __getitem__()
m.seek(0)
print repr(m[0:5])
print repr(m[5:10])
print repr(m[4])

# Test get/putvalue()
# Note: A string is the same thing as a character sequence.
print repr(m.getvalue())
m.seek(0)
m[:] = 'MMM'
m.seek(0)
print repr(m.getvalue())

# Test flush(), write(), and commi
