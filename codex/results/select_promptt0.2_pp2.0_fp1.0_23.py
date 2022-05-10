import select
# Test select.select()

# select.select() takes three lists of file descriptors:
#   - The first list is for file descriptors to check for being ready for reading
#   - The second list is for file descriptors to check for being ready for writing
#   - The third list is for file descriptors to check for having an exception condition pending
#
# select.select() returns a tuple of three lists:
#   - The first list contains the file descriptors that are ready for reading
#   - The second list contains the file descriptors that are ready for writing
#   - The third list contains the file descriptors that have an exception condition pending

# The file descriptors in the lists returned by select.select() are the same as those passed in.
# The file descriptors in the lists returned by select.select() are in the same order as those passed in.
# The file descriptors in the lists returned by select.select() are not necessarily in any particular order.
# The file descriptors in the lists returned by select.select() are not necessarily unique.

# The file descriptors in the lists returned by select.select() are not necessarily the same as
