import select
# Test select.select() function
# select.select() can monitor multiple file descriptors
# and fire when any of them is ready
# file descriptor is an integer index to I/O device that
# the kernel uses as a handle for I/O operation and
# as a key for filing I/O information
# In this case I use sys.stdin
# It will fire when user press ENTER
print("I'm going to read from sys.stdin...")
print("Press ENTER to fire the select()")

ready = select.select([sys.stdin], [], [], 5)

if ready[0]:
    print("Fire!")

print("Done!")
