import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# Return three lists of objects that are ready for reading, writing, or error handling.

# rlist: select will return when one or more file descriptors in this list is ready for reading.
# wlist: select will return when one or more file descriptors in this list is ready for writing.
# xlist: select will return when one or more file descriptors in this list has an error.
# timeout(float): select will return when this time has expired.
# If None, select will block until a file descriptor is ready.
# If 0, select will return immediately.
# If negative, select will block indefinitely.

# Return value: three lists, the first contains objects that are ready for reading, the second for writing, and the third for error handling.

# select.select() is a blocking function. It means that the function will not return until objects in rlist or wlist are ready.
# select.select() will raise an OSError exception if the file descriptor is invalid.

# select.select() supports file descriptors in all platforms.
