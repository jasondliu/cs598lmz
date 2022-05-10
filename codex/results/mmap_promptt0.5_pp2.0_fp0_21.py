import mmap
# Test mmap.mmap(0,1) 
# on Windows, this is an invalid call, but it is valid on Linux.
# On Windows, this call will raise a ValueError exception.
try:
    m = mmap.mmap(0,1)
except ValueError:
    print("ValueError raised when mmap(0,1)")
else:
    print("No ValueError raised when mmap(0,1)")

# Test mmap.mmap(-1,1) 
# on Windows, this is an invalid call, but it is valid on Linux.
# On Windows, this call will raise a ValueError exception.
try:
    m = mmap.mmap(-1,1)
except ValueError:
    print("ValueError raised when mmap(-1,1)")
else:
    print("No ValueError raised when mmap(-1,1)")

# Test mmap.mmap(0,0) 
# on Windows, this is an invalid call, but it is valid on Linux.
# On Windows, this call will raise a ValueError exception.
try:
    m =
