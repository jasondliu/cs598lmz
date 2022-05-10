import mmap
# Test mmap.mmap - does it work?

# I'm disappointed to see this doesn't work

#d = mmap.mmap(-1, 100)
#d.write("\x00"*100)
#d[0] = 1
#d[1] = 2
#d[2] = 3
#d[3] = 4
#print map(ord, d[0:10])
#print map(ord, d[0:10])
