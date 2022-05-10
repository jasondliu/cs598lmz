import select
# Test select.select
rfds, wfds, efds = select.select([] , [], [], 1)
print("rfds: ", rfds)
print("wfds: ", wfds)
print("efds: ", efds)

# Test select.poll
p = select.poll()
p.register(sys.stdin)
p.poll()
print("poll: ", p.poll())

# Test select.epoll
epoll = select.epoll()
epoll.poll()
print("epoll: ", epoll.poll())

# Test select.devpoll
dp = select.devpoll()
dp.poll()
print("devpoll: ", dp.poll())

# Test select.kqueue
kq = select.kqueue()
kq.control([], 1, 0)
print("kqueue: ", kq.control([], 1, 0))

# Test select.kevent
kevent = select.kevent(sys.stdin, select.KQ_FILTER_READ)
