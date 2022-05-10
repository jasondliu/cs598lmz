import select
# Test select.select
# https://docs.python.org/3/library/select.html
# https://docs.python.org/3/library/selectors.html

# select.select is a low-level function that can be used to wait for
# a file descriptor to become ready.
# select.select() will monitor a set of file descriptors and return
# when one or more of them become ready.
# select.select() accepts three lists as arguments:
#   the first list contains the file descriptors to be monitored for
#       being ready to read
#   the second list contains the file descriptors to be monitored for
#       being ready to write
#   the third list contains the file descriptors to be monitored for
#       error conditions
# select.select() returns three lists:
#   the first list contains the file descriptors that are ready to read
#   the second list contains the file descriptors that are ready to write
#   the third list contains the file descriptors that have an error

# So you have to have 3 lists.  These lists can be empty.
# If a list is empty, select.select() will block
