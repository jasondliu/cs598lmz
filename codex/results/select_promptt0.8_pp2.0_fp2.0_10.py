import select
# Test select.select()
read, write, error = select.select([sys.stdin], [], [], 1)
print read, write, error
# Test select.poll()
p = select.poll()
p.register(sys.stdin, select.POLLIN)
events = p.poll(1000)
print events

# Test select.epoll()
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
events = epoll.poll(1)
print events

# Test select.kqueue()
kqueue = select.kqueue()
kqueue.control([select.kevent(sys.stdin, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
events = kqueue.control(None, 1)
print events

# Test select.devpoll()
try:
	dp = select.devpoll()
	dp.register(sys.stdin, select.POLLIN)
	events = dp.poll(1000)
	print events
except:
	print "
