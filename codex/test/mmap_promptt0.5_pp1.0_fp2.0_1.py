import mmap
# Test mmap.mmap(0, 1)
with mmap.mmap(0, 1) as m:
    pass

# Test mmap.mmap(0, 1, "r")
with mmap.mmap(0, 1, "r") as m:
    pass

# Test mmap.mmap(0, 1, "r+")
with mmap.mmap(0, 1, "r+") as m:
    pass

# Test mmap.mmap(0, 1, "w")
with mmap.mmap(0, 1, "w") as m:
    pass

# Test mmap.mmap(0, 1, "w+")
with mmap.mmap(0, 1, "w+") as m:
    pass

# Test mmap.mmap(0, 1, "c")
with mmap.mmap(0, 1, "c") as m:
    pass

# Test mmap.mmap(0, 1, "c+")
