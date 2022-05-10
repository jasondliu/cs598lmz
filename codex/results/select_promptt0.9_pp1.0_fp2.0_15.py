import select
# Test select.select()
# MySQL server ready to work
# select.select(rlist, wlist, xlist[, timeout])
# rlist – list of clients to watch for reading
# wlist – list of clients to watch for writing
# xlist – list of clients to watch for exceptions
# timeout - timeout values in seconds (default - block)
# Function returns 3 lists:
# rlist -- list of clients in rlist that have data available for reading
# wlist -- list of clients in wlist, ready for writing
# xlist -- lists of clients that are exceptional
# If returned list is empty, then either timeout happened or something's wrong with clients in the list


# Create our listening socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((HOST, PORT))

# Set socket in listen mode
sock.listen()

# List to keep track of sockets for select.select()
socket_list = [sys
