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
