import select
# Test select.select()
#
# select.select() takes three lists of file descriptors:
#
#   - The first is the list of file descriptors to be checked for
#     being ready to read.
#
#   - The second is the list of file descriptors to be checked for
#     being ready to write.
#
#   - The third is the list of file descriptors to be checked for
#     error conditions.
#
# It returns a tuple of three lists:
#
#   - The first list contains the file descriptors that are ready to
#     read.
#
#   - The second list contains the file descriptors that are ready to
#     write.
#
#   - The third list contains the file descriptors that have error
#     conditions.
#
# select.select() is a blocking call. It will not return until at
# least one file descriptor is ready to read, ready to write, or has
# an error condition.
#
# In this example, we set up two pipes, one for reading and one for
# writing. We then use select.select() to wait for the pipe to
