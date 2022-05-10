import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, select() can block indefinitely

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output
# select.select() can be used to implement a simple single-threaded web server

# Example:
# A simple single-threaded web server
# The server handles only one client at a time
# The server handles only one request per connection
# The server does not handle POST requests
# The server does not handle any headers other than Content-Length
# The server does not handle persistent connections
# The server does not handle any HTTP request other than GET
# The server does not handle any HTTP version other than 1.0

# The server is implemented in a single file, select_echo_server.py

