import mmap
# Test mmap.mmap.read(int) behavior

# read(integer) should return string of length integer. 
# It should not exceed the bounds of the map.
#
# Modified by A.S. 2011-12-13

f = open('data', 'w+')
f.write('abcdefghi')
f.close()

f = open('data', 'r+')
mm = mmap.mmap(f.fileno(), 0)

assert mm.read(1) == 'a'
assert mm.read(1) == 'b'
assert mm.read(2) == 'cd'
assert mm.read(3) == 'efg'
assert mm.read(4) == 'hi'

f.close()
try:
    mm = None
except TypeError:
    pass
