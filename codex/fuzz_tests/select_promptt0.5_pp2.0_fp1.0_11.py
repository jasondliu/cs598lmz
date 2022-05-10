import select
# Test select.select
# select.select([], [], [], 3)

# Test select.poll
# p = select.poll()
# p.register(sys.stdin, select.POLLIN)
# p.poll(3)

# Test select.epoll
# e = select.epoll()
# e.register(sys.stdin, select.EPOLLIN)
# e.poll(3)

# Test select.kqueue
# k = select.kqueue()
# k.control([select.kevent(sys.stdin, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0, 3)

# Test select.devpoll
# import os
# d = select.devpoll()
# d.register(os.open(__file__, os.O_RDONLY), select.POLLIN)
# d.poll(3)

# Test select.select
# select.select([], [], [], 3)

# Test select.poll
# p = select.poll()
# p.register(sys.stdin
