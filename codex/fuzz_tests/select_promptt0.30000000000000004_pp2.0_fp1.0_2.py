import select
# Test select.select()

# The select() function takes three lists of file descriptors and waits until
# one or more of the descriptors is ready for some kind of I/O. The first list
# passed to select() is a list of the descriptors to be checked for being ready
# to read. The second list is a list of descriptors to be checked for being
# ready for writing. The third list is a list of descriptors to be checked for
# error conditions.

# The select() function returns three lists of file descriptors. The first list
# contains the descriptors that are ready for reading. The second list contains
# the descriptors that are ready for writing. The third list contains the
# descriptors that have an error condition.

# The select() function can be used to implement a simple timeout. If all three
# lists passed to select() are empty, then select() blocks until at least one of
# the descriptors becomes ready. But if the timeout parameter is provided, then
# select() will block for at most that many seconds. If the timeout expires
# before any of the descriptors become ready, then three empty lists are
# returned.

