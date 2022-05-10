import select
# Test select.select method.
# It has three parameters.
# An first parameter is a list of sockets to be watched for readability.
# An second parameter is a list of sockets to be watched for writability.
# An third parameter is a list of sockets to be watched for errors.

# select.select returns a list of 3 lists.
# They are lists of sockets that are now readable, writable or in error.
# The order of each list is the same as the order in the corresponding list of the original parameters.
# If a socket is ready for more than one type of operation, it will be contained in more than one list.

# select.select is blocking.



def server(port, delay=0.0):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setsockopt is a method to set socket options.
    sock.bind(('', port))
    sock.listen(1)
    while True:
        connection, address = sock.accept()
        print('connection: ', connection)
        print('
