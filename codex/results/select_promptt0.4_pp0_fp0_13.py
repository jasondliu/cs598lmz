import select
# Test select.select()
#
# select.select() is a function that monitors a set of file descriptors (FDs)
# and returns a list of the FDs that are ready for reading, writing, or
# have an error.
#
# The FDs in the set of FDs to monitor are passed in as a list of three
# lists:
#
#   select.select(read_fds, write_fds, error_fds, timeout)
#
# where read_fds is a list of FDs to monitor for reading, write_fds is a list
# of FDs to monitor for writing, and error_fds is a list of FDs to monitor for
# errors.
#
# The return value is a list of three lists:
#
#   read_ready, write_ready, error_ready = select.select(read_fds, write_fds, error_fds, timeout)
#
# where read_ready is a list of FDs that are ready for reading, write_ready is
# a list of FDs that are ready for writing, and error_ready is a list of FD
