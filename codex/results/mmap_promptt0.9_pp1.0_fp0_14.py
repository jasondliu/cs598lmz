import mmap
# Test mmap.mmap(fd, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0) 
filename = './output/mmap_test'
size = 1024
# Write a byte each 0.05 sec.
for i in range(size):
    time.sleep(0.05)
    with open(filename,'ab') as f:
        f.write((str(unichr(random.randint(32,255)))))

# Read content 
with open(filename,'r+b') as f:
    # memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    #m.readline()  # b'This is the first line of the file.\n'
    while True:
        line = m.readline()
        if not line:
            break
        print(line)
    # read content via slice notation
    #print(m[:5])  # b'hello'
    # close the map
m.close()
