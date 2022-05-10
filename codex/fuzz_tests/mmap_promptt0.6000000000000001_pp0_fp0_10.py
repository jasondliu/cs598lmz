import mmap
# Test mmap.mmap()

# create
f = open('hello.txt', 'w+')
f.write('hello world!')
f.close()

# open
f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write(b'hello mmap!')

# read
m.seek(0)
print(m.readline())

# close
m.close()
f.close()

# delete
os.remove('hello.txt')

# test mmap.mmap()'s size
f = open('test.txt', 'w+')
f.write('hello world!')
f.close()

f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.size())
m.close()
f.close()

# delete
os.remove('test.txt')

# test mmap.mmap()'s access
f = open('test.txt',
