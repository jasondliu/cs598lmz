import select
# Test select.select()
while test.flag:
    inputready, outputready, exceptready = select.select(input, [], [])

# Test select.poll(), select.epoll(), and select.kqueue()
p = select.poll()
p.register(input[0], select.POLLIN)
while test.flag:
    p.poll()

ep = select.epoll()
ep.register(input[0], select.EPOLLIN)
while test.flag:
    ep.poll()

kq = select.kqueue()
kq.control([select.kevent(input[0], filter=select.KQ_FILTER_READ)], 1, 0)
while test.flag:
    kq.control(None, 1, 0)

# Test select.devpoll()
d = select.devpoll()
d.register(input[0], select.POLLIN)
while test.flag:
    d.poll()

# Test select.select()
select.select(input, [], [])
select.select(input, [], [], 0.
