import select
# Test select.select
print(select.select([], [], [], 0))

# Test select.poll
poll = select.poll()
poll.register(1, select.POLLIN)
poll.poll(0)

# Test select.epoll
epoll = select.epoll()
epoll.register(1, select.EPOLLIN)
epoll.poll(0)

# Test select.kqueue
kqueue = select.kqueue()
kevent = select.kevent(1, filter=select.KQ_FILTER_READ)
kqueue.control([kevent], 0)

# Test select.devpoll
devpoll = select.devpoll()
devpoll.register(1, select.POLLIN)
devpoll.poll(0)

# Test select.select
print(select.select([], [], [], 0))

# Test select.poll
poll = select.poll()
poll.register(1, select.POLLIN)
poll.poll(0)
