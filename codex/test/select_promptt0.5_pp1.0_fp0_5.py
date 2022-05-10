import select
# Test select.select()
# https://docs.python.org/2/library/select.html
# https://docs.python.org/3/library/select.html
#
# In Python 2, select.select() returns three lists of objects.
# In Python 3, select.select() returns three lists of file descriptors.
#
# In Python 2, select.select() can be used with sockets.
# In Python 3, select.select() can be used with sockets and other file-like objects.
#
# In Python 2, select.select() uses file descriptors.
# In Python 3, select.select() uses file descriptors and handles.
#
# In Python 2, select.select() can be used with sockets, pipes and files.
# In Python 3, select.select() can be used with sockets, pipes, files and other file-like objects.
#
# In Python 2, select.select() uses file descriptors.
# In Python 3, select.select() uses file descriptors and handles.

# Create a TCP/IP socket
