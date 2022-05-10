import select
# Test select.select
print(select.select([sys.stdin], [], [], 0.0)[0])

# Test select.epoll
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
print(epoll.poll(0.0))

# Test select.poll
poll = select.poll()
poll.register(sys.stdin.fileno(), select.POLLIN)
print(poll.poll(0.0))

# Test select.kqueue
kqueue = select.kqueue()
kqueue.control([select.kevent(sys.stdin, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0, 0)
print(kqueue.control(None, 1, 0))

# Test select.devpoll
devpoll = select.devpoll()
devpoll.register(sys.stdin.fileno(), select.POLLIN)
print(devpoll.poll(0.0))

# Test select.select
# select.select([sys.stdin], [
