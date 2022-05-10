import mmap
# Test mmap.mmap...
print int(pow(mmap.PAGESIZE,2)*2 + 4)
print '1'*int(pow(mmap.PAGESIZE,2)*2 + 4) == '1'*int(pow(mmap.PAGESIZE,2)*2 + 4)
snr = '''
m = mmap.mmap(fd, 0)

print '1'*int(pow(mmap.PAGESIZE,2)*2 + 4)
print '1'*int(pow(mmap.PAGESIZE,2)*2 + 4) == '1'*int(pow(mmap.PAGESIZE,2)*2 + 4)

m.close()
'''

from sys import argv
fname = argv[1]

#from mmap import mmap, PROT_READ
f = open(fname, "r")
# Use mmap to read file into memory where available
#m = mmap(f.fileno(), 0, prot=PROT_READ)
m = mmap.mmap(f.fileno(),
