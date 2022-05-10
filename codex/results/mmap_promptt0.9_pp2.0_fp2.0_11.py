import mmap
# Test mmap.mmap(-1, 13)

print "about to open file..."
f = open('foo', 'w+')
mapf = mmap.mmap(f.fileno(), 13)
print "about to write..."
mapf.write('hello there\n')
print mapf.readline()
print "wakka"
print mapf[0:5]
print "wakka2"
print mapf.read(1)
print "wakka3"
print mapf.readline()
print "wakka4"
print mapf.readline()
print "wakka5"
mapf[6:] = 'world\n'
print mapf.readline()      # prints 'world\n'
print mapf.readline()      # prints 'world\n'
mapf.seek(0)               # rewind
print mapf.readline()      # prints 'hello world\n'
mapf.close()

f.close()

# Should print "hello there" then "world"

###################################################################

# check mmap.mmap() arguments
