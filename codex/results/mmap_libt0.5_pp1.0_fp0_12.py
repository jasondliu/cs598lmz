import mmap

# Read file
f = open('/home/siddharth/Downloads/test.txt', 'r')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Iterate over each line
for line in iter(s.readline, ""):
    print line
</code>

