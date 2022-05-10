import select
# Test select.select()
rlist = []
wlist = [sys.stdout]
xlist = []
ret = select.select(rlist, wlist, xlist)
print(ret)
# Test select.poll()
poll = select.poll()
events = poll.poll(1000)
print(events)
# Test select.epoll()
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN|select.EPOLLET)
events = epoll.poll(1000)
print(events)
# Test select.kqueue()
kq = select.kqueue()
kev = select.kevent(sys.stdin.fileno(),
                    select.KQ_FILTER_READ,
                    select.KQ_EV_ADD | select.KQ_EV_ENABLE)
events = kq.control([kev], 1, None)
print(events)
