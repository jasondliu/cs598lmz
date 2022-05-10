import mmap
# Test mmap.mmap using interned strings as keys.
msg = mmap.mmap(-1, 1024)
c1 = 'abc'
c2 = 'abcd'
c3 = 'abcde'
msg[c1] = c1
