import mmap
# Test mmap.mmap()
#
#    >>> import mmap
#    >>> m = mmap.mmap(-1, 1)
#    >>> m.write("a")
#    1

#    >>> m.seek(0)
#    0
#    >>> m.read(1)
#    'a'
#    >>> m.close()

# Test mmap.mmap(fd, length)
#
#    >>> f = open('mmaptest.txt', 'w+')
#    >>> f.write('Hello Python!')
#    >>> f.close()
#
#    >>> f = open('mmaptest.txt', 'r+')
#    >>> m = mmap.mmap(f.fileno(), 13)
#    >>> m.read(1)
#    'H'
#    >>> m.seek(6)
#    6
#    >>> m.read(1)
#    'P'
#    >>> m.read(7)
#    'ython!'
#    >>> m.seek(len(m))
#    13
#    >>> m
