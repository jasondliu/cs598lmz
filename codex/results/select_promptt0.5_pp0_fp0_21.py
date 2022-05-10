import select
# Test select.select()

# select.select(r, w, e, timeout)
# r, w, e are lists of IO streams, which select() will wait for
# For example, if r is not empty, select() will wait for an IO stream in r to be ready for reading
# If timeout is not None, select() will wait for at most timeout seconds
# If timeout is None, select() will wait indefinitely

# select.select() returns three lists:
# The first list contains the IO streams ready for reading
# The second list contains the IO streams ready for writing
# The third list contains the IO streams with errors

# select.select() is useful for multiplexing IO streams
# For example, if we want to wait for user input and also wait for a TCP socket to be ready for reading,
# we can use select.select() to wait for both events to happen
# select.select() is also useful for implementing timeouts

# Let's implement a simple select.select() example
# We will create a TCP server, which will echo back the data it receives
# We will also create a TCP client, which will send some data to the server and
