import mmap
# Test mmap.mmap

f = open('/Users/leo/Downloads/150-0.txt', 'r+b')
m = mmap.mmap(f.fileno(), 0)


print('Original content:', m.readline().rstrip())  # prints "Hello Python!"

m.seek(0)
m.write(b'Hello World!')
m.seek(0)
print('Modified content:', m.readline().rstrip())  # prints "Hello World!"

m.close()
