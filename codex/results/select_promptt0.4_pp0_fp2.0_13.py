import select
# Test select.select
# select.select([], [], [], 0)

# Test select.poll
# p = select.poll()
# p.register(0, select.POLLIN)
# p.poll(0)

# Test select.epoll
# e = select.epoll()
# e.register(0, select.EPOLLIN)
# e.poll(0)

# Test select.kqueue
# k = select.kqueue()
# k.control([], 0, 0)

# Test select.devpoll
# d = select.devpoll()
# d.register(0, select.POLLIN)
# d.poll(0)

# Test select.kevent
# k = select.kqueue()
# k.control([select.kevent(0, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0, 0)

# Test select.select
# select.select([], [], [], 0)

# Test select.poll
# p = select.poll()
# p.register(0, select
