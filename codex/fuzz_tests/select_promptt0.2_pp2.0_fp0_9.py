import select
# Test select.select()

# select.select() takes three lists of file descriptors:
#   1. The first list is the list of file descriptors to be watched for being
#      ready to read.
#   2. The second list is the list of file descriptors to be watched for being
#      ready to write.
#   3. The third list is the list of file descriptors to be watched for error
#      conditions.
# It returns three lists of file descriptors:
#   1. The first list is the list of file descriptors that are ready to read.
#   2. The second list is the list of file descriptors that are ready to write.
#   3. The third list is the list of file descriptors that have error
#      conditions.
#
# The timeout argument is the maximum time to wait for any file descriptor to
# become ready.  If timeout is None, then select.select() will block until
# some file descriptor becomes ready.
#
# select.select() is a blocking call.  It will block until some file descriptor
# becomes ready or until the timeout expires.
#
# select.select()
