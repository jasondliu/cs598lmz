import select
# Test select.select()
#
# select.select() is used to monitor multiple file descriptors, waiting until one or more of the file descriptors become "ready" for some class of I/O operation (e.g. input possible).
#
# The first three arguments to select() are three lists of file descriptors to be monitored. The first list contains the file descriptors to be checked for being "ready for reading", the second contains the file descriptors to be checked for being "ready for writing", and the third contains the file descriptors to be checked for errors.
#
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. The first list contains the objects that are ready for reading, the second contains the objects that are ready for writing, and the third contains the objects that have an exceptional condition (e.g. there is out-of-band data available to read).
#
# The optional fourth argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds. If it is absent or None, the call will never time out.
#
# The return value is a triple of lists of objects that are ready:
