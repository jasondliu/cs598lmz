import select
# Test select.select()

# select.select() takes three arguments:
# 1. a list of file descriptors to check for readability
# 2. a list of file descriptors to check for writability
# 3. a list of file descriptors to check for errors
# It returns three lists of file descriptors that are ready for reading, writing, and errors.

# select.select() is a blocking call, meaning that it will wait until at least one of the file descriptors is ready.
# If you want to set a timeout, you can pass a fourth argument, which is the timeout in seconds.

# Example:
# import socket
# import select
#
# s = socket.socket()
# s.bind(('localhost', 5000))
# s.listen(5)
#
# while True:
#     rlist, wlist, xlist = select.select([s], [], [])
#     for r in rlist:
#         conn, addr = r.accept()
#         print('Got connection from', addr)
#         conn.close()

# select.select() is a useful tool for building network servers
