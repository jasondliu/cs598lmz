import select
# Test select.select
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
print 'Press a key'
poller.poll()
print 'Thank you'

# Test select.epoll
# Python 2.6+ required
epoller = select.epoll()
epoller.register(sys.stdin, select.EPOLLIN)
print 'Press a key'
epoller.poll()
print 'Thank you'
# Test select.kqueue
# Python 2.6+ required
kqueue = select.kqueue()
kqueue.control([select.kevent(sys.stdin, filter=select.KQ_FILTER_READ,
                              flags=select.KQ_EV_ADD)], 0)
print 'Press a key'
kqueue.control(None, 1)
print 'Thank you'
