import mmap
# Test mmap.mmap
with open('_test/build/test-1-output.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:14]= "This is a test"
    m.seek(0)
    print ('mmap: '+ m.read(14))

# Test mmap.ACCESS_READ
#
# View a read access memory mapped object.
#
with open('_test/build/test-1-output.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print ('access_read: ' + str(m.find('This')))

# Test mmap.ACCESS_COPY
with open('_test/build/test-1-output.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    print ('access_copy: '+ str(m.find('This
