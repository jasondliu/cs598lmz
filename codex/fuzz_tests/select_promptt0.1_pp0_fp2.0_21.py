import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    # On Unix, we can use a pair of connected sockets
    # as a way to send data between two threads.
    # The parent process creates a pair of connected sockets,
    # and then forks a child process.  The child inherits
    # the connected sockets.  The parent and child can then
    # send data back and forth over the sockets.
    #
    # This is a simple way to communicate between processes,
    # but it has some limitations.  For example, the total
    # amount of data that can be sent is limited to 64K on
    # many systems.  Also, the sockets can only be used for
    # communication between processes on the same machine.
    #
    # The sockets can be used for communication between
    # threads in the same process, but that's not very useful.
    #
    # The sockets can also be used for interprocess
    # communication on Windows, but that's not very useful
    # either, since Windows already has named pipes.

    parent, child = socket.socket
