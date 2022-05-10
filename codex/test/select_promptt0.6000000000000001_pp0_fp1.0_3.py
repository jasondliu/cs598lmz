import select
# Test select.select
# select.select([sys.stdin], [], [], 2)
# select.select([sys.stdin], [], [], 2)
# select.select([sys.stdin], [], [], 2)

# Test select.poll
# poll = select.poll()
# poll.register(sys.stdin.fileno(), select.POLLIN)
# poll.poll(1000)
# poll.poll(1000)
# poll.poll(1000)

# Test select.epoll
# epoll = select.epoll()
# epoll.register(sys.stdin.fileno(), select.EPOLLIN)
# epoll.poll(1000)
# epoll.poll(1000)
# epoll.poll(1000)

# Test select.kqueue
# kqueue = select.kqueue()
# kqueue.control([select.kevent(sys.stdin.fileno(), select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
# kqueue.control(None, 5)
# kqueue.control(
