import select
# Test select.select()

import select, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 25000))
s.listen(5)
while True:
    # select() is non-blocking
    # select() will block until there is a new connection
    # Once there is a new connection, it will append to the list
    # and will stop blocking
    # select() will return a list of socket objects that are ready
    # to be read from (i.e. new connection)
    # It will also return a list of socket objects that are ready
    # to be written to (i.e. established connection)
    # It will also return a list of socket objects that have raised
    # an exception (i.e. established connection)
    # select() takes a timeout parameter that is in seconds
    # The default timeout is None which means it will block indefinitely
    # If timeout is 0, it will block for a minimum amount of time
    # If timeout is greater than 0, it will block for the specified amount of time
    # If timeout is less
