import select
# Test select.select()
# select.select() is a low-level method, which is used by the higher-level
# methods in the socket module.
# select.select() is a blocking call, which means that the program will wait
# until the socket is ready for reading/writing.
# select.select() takes three parameters: three lists of sockets.
# The first list contains the sockets that will be checked for readiness to
# be read from.
# The second list contains the sockets that will be checked for readiness to
# be written to.
# The third list contains the sockets that will be checked for any errors.
# The three lists are checked in parallel, and select.select() will return
# three lists of sockets that are ready for reading/writing/errors.
# If the timeout is omitted, then select.select() will block indefinitely.
# If the timeout is 0.0, then select.select() will return immediately.
# If the timeout is > 0.0, then select.select() will block for that amount
# of time.
# If the timeout is < 0.0, then select.select() will block indefinitely.

# Test select.select
