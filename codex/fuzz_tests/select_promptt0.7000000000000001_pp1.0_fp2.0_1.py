import select
# Test select.select
print select.select([], [], [], 0.1)

# Test select.poll
p = select.poll()

# Test select.epoll
epoll = select.epoll()
epoll.register(1, select.EPOLLIN)
epoll.poll(0.1)

# Test select.kqueue
kqueue = select.kqueue()
kqueue.control([select.kevent(10, select.KQ_FILTER_READ)], 0.1)
