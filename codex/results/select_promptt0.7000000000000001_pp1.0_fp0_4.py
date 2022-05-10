import select
# Test select.select()
    #select.select([input], [], [])
# Test select.poll()
    #poll = select.poll()
    #poll.register(input, select.POLLIN)

#from select import poll, POLLIN
#poller = poll()
#poller.register(input, POLLIN)

from select import epoll, EPOLLIN
poller = epoll()
poller.register(input, EPOLLIN)

# Wait for at least one of the sockets to be ready for processing
print 'Waiting for the next event'
while True:
    # Different from select
    #events = poller.poll()
    events = poller.poll(1)
    for fileno, event in events:
        # Handle inputs
        if fileno == input.fileno():
            # A "readable" server socket is ready to accept a connection
            connection, address = input.accept()
            print '  Connection', address
            connection.setblocking(0)
            poller.register(connection, EPOLLIN)
        elif event & EPO
