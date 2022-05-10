import select
# Test select.select()
# https://docs.python.org/3/library/select.html
# https://docs.python.org/3/library/select.html#select.select

# The select() function is a direct interface to the underlying operating system
# implementation of select(). It does not provide a portable interface across
# operating systems.
# The function select() is a very useful function for a network server.
# It allows the server to monitor multiple sockets and to know when data arrives on one of the sockets.

# The select() method is a way to ask the operating system if one or more sockets are ready for I/O.
# For example, imagine you have a list of sockets that you want to monitor.
# You want to know if you can read from the sockets (receive data) or write to the sockets (send data).
# Use the select() method to find out which sockets are ready for reading or writing.
# Note that the select() method only works on Windows and Unix-like operating systems.
# If you are working on other systems, you can use the setblocking() method to make the socket non-blocking.
# This way you can use
