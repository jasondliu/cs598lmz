import select
# Test select.select()
print('select.select(): ', select.select.__doc__)
rlist, wlist, xlist = select.select([], [], [], 0)
print('rlist: ', rlist)
print('wlist: ', wlist)
print('xlist: ', xlist)

# Test select.poll()
print('select.poll(): ', select.poll.__doc__)
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
poll_result = poller.poll()
print('poll_result: ', poll_result)

# Test select.epoll()
print('select.epoll(): ', select.epoll.__doc__)
epoller = select.epoll()
epoller.register(sys.stdin.fileno(), select.EPOLLIN)
epoll_results = epoller.poll()
print('epoll_results: ', epoll_results)

# Test select.kqueue()
print('select.kqueue(): ', select.kqueue.__doc__)
kqueue = select.k
