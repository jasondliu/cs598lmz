import mmap

# open the file in readonly mode
f = open('test.txt', 'r')

# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
#print mm.readline()  # prints "Hello Python!"

# read content via slice notation
#print mm[:5]  # prints "Hello"

# close the map
#mm.close()

# open the file in readonly mode
f = open('test.txt', 'r')

# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
#print mm.readline()  # prints "Hello Python!"

# read content via slice notation
#print mm[:5]  # prints "Hello"

# close the map
#mm.close()

# open the file in readonly mode
f = open('test.txt', 'r')

# memory-map the file, size 0 means whole
