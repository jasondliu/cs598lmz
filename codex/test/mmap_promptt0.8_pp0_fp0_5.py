import mmap
# Test mmap.mmap()
memmap = mmap.mmap(-1, 100)
memmap

# The code below will throw an exception:
# memmap[0] = b'H'
# memmap.close()

# The code below works:
memmap = mmap.mmap(-1, 100, access=mmap.ACCESS_WRITE)
memmap[0] = b'H'
memmap.close()

memmap = mmap.mmap(-1, 100, access=mmap.ACCESS_READ)
memmap[0] = b'H'
memmap.close()

# The code below will throw an exception:
# memmap[0] = b'H'
# The reason is that the mmap() function accepts only one access argument.
