import mmap
# Test mmap.mmap(0, 1, prot=mmap.PROT_READ)
try:
    mmap.mmap(0, 1, prot=mmap.PROT_READ)
except ValueError:
    # It's ok
    pass
else:
    print("Could create mmap with PROT_NONE")

try:
    mmap.mmap(0, 1, flags=mmap.MAP_ANONYMOUS, prot=mmap.PROT_NONE)
except ValueError:
    # It's ok
    pass
else:
    print("Could create mmap with PROT_NONE")

# Test mmap.mmap(-1, 1)
try:
    mmap.mmap(-1, 1)
except ValueError:
    # It's ok
    pass
else:
    print("Could create mmap with file=-1")

if sys.platform == 'win32':
    # Test invalid handle
    try:
        mmap.mmap(-2, 1)
    except ValueError:
        # It's ok
        pass
    else:
        print
