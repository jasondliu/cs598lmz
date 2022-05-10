import select
# Test select.select()

# select() takes 3 lists:
#   1. The first list contains the objects to be checked for incoming data.
#   2. The second list contains the objects to be checked for outgoing data.
#   3. The third list contains the objects to be checked for errors.

# select() returns 3 lists:
#   1. The first list contains the objects that have incoming data.
#   2. The second list contains the objects that are ready to send data.
#   3. The third list contains the objects that have errors.

# select() also takes a 4th parameter, which is the timeout.
# If the timeout is 0, then select() will return immediately.
# If the timeout is None, then select() will wait indefinitely.

# select() is a blocking call.

# select() can be used for any kind of stream, including sockets.

# select() is available on Windows, Linux, and macOS.
# select() is NOT available on BSD.

# select() can be used with sockets, pipes, and files.

# select() is NOT thread-safe.

# select() is NOT
