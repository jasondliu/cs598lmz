import mmap
# Test mmap.mmap()

mm = mmap.mmap(1, 2)

# Test mmap.ACCESS_COPY

mm = mmap.mmap(1, 2, mmap.ACCESS_COPY)

# Test mmap.ACCESS_READ

mm = mmap.mmap(1, 2, mmap.ACCESS_READ)

# Test mmap.ACCESS_WRITE

mm = mmap.mmap(1, 2, mmap.ACCESS_WRITE)


# Test mmap.ALLOCATIONGRANULARITY

mmap.ALLOCATIONGRANULARITY


# Test mmap.close()

mm = mmap.mmap(1, 2)
mm.close()


# Test mmap.find()

mm = mmap.mmap(1, 2)
mm.find(1)
mm.find(1, 3, 4)


# Test mmap.flush()

mm = mmap.mmap(1, 2)
mm.flush()
