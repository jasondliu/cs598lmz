import select
# Test select.select()

# select.select() takes three arguments: three lists of objects to be monitored.
# The first list contains the objects to be monitored for incoming data,
# the second for outgoing data, and the third for "exceptional conditions"
# (this last list is optional).
# select.select() returns three lists containing subsets of the first three arguments.
# The first list contains objects that are ready for reading,
# the second for writing, and the third for errors.
# If the timeout argument is omitted, select.select() blocks until at least one of the monitored objects is ready.
# If the timeout argument is a number, it specifies a timeout in seconds.
# When the timeout argument is a floating point number,
# it specifies a timeout in seconds and microseconds.
# If the timeout argument is omitted or None, the behavior is the same as when the timeout argument is zero.
# The return value is a triple of lists of objects that are ready:
# subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready,
# three empty lists are returned.
# A file descriptor is considered ready if it
