import mmap
# Test mmap.mmap
# mmap.mmap(fileno, length, access=mmap.ACCESS_RW, offset=0)

# the line below needs to be changed to point to the correct file
# f = open('map_test.txt', 'r+b')
# m = mmap.mmap(f.fileno(), 0)
# print m.readline()
# m.seek(0)
# m.write('0123456789abcdef')
# m.seek(0)

# m.write('/n'.encode('utf-8'))
# m.write('This is a new line.'.encode('utf-8'))
# m.close()

# print m.readline()
# print m.readline()
# print m.readline()

# m = mmap.mmap(-1, 8)
# m[4:8] = 'spam'

# m = mmap.mmap(-1,16)
# m.write('hello world\n')
# m.seek(0) # rewind
# while True:
