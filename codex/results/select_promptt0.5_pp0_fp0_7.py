import select
# Test select.select()

# The select() call is a way to ask the OS which file descriptors are ready for reading,
# writing, or have an error.
#
# The select() call takes three lists of file descriptors:
# - the first list is the read list, which is the list of file descriptors that you want to check
#   to see if they are ready for reading
# - the second list is the write list, which is the list of file descriptors that you want to check
#   to see if they are ready for writing
# - the third list is the error list, which is the list of file descriptors that you want to check
#   to see if they have an error
#
# The select() call returns three lists of file descriptors:
# - the first list is the read list, which is the list of file descriptors that are ready for reading
# - the second list is the write list, which is the list of file descriptors that are ready for writing
# - the third list is the error list, which is the list of file descriptors that have an error
#
# If the timeout is 0, then select() will not
