import select
# Test select.select()
#
# select() takes three lists of file descriptors.
# It blocks until one of the file descriptors is ready for some kind of I/O.
# The first list contains file descriptors that you want to check for readability.
# The second list contains file descriptors that you want to check for writability.
# The third list contains file descriptors that you want to check for an "exceptional condition".
#
# select() returns three lists of file descriptors.  The first contains the descriptors that are ready for reading.
# The second contains the descriptors that are ready for writing.
# The third contains the descriptors that have an exceptional condition.
#
# select() can also be used with sockets.
#
# In this example, we will use select() to monitor the keyboard input and a socket at the same time.
#
# When select() returns, we will check which file descriptors are ready
# and then we will act accordingly.
#
# This example is a simple echo server.
# It will listen on localhost:9999 and when a client connects to it, it will send back to the client whatever it receives.
