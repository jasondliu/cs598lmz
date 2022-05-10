import select
# Test select.select()
#
# select.select() takes three lists of file descriptors and waits until
# some of them are ready for reading, ready for writing, or have an
# error condition.
#
# The first list is the list of file descriptors to check for reading.
# The second list is the list of file descriptors to check for writing.
# The third list is the list of file descriptors to check for errors.
#
# select.select() returns three lists of file descriptors.
# The first list is the list of file descriptors that are ready for reading.
# The second list is the list of file descriptors that are ready for writing.
# The third list is the list of file descriptors that have an error condition.
#
# select.select() takes an optional fourth parameter, which is the timeout.
# If the timeout is 0, select.select() will return immediately.
# If the timeout is None, select.select() will wait indefinitely.
# If the timeout is a positive number, select.select() will wait up to that
# number of seconds.
#
# select.select() will raise an exception if the lists
