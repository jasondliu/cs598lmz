import select
# Test select.select
# select.select([], [], [], 0)

# Test select.poll
# p = select.poll()
# p.poll(0)

# Test select.epoll
# e = select.epoll()
# e.poll(0)

# Test select.kqueue
# k = select.kqueue()
# k.control([], 0)

# Test select.devpoll
# d = select.devpoll()
# d.poll(0)

# Test select.kevent
# k = select.kevent(0, 0, 0)
# k.ident
# k.filter
# k.flags
# k.fflags
# k.data
# k.udata

# Test select.kevent.flags
# select.KQ_EV_ADD
# select.KQ_EV_DELETE
# select.KQ_EV_ENABLE
# select.KQ_EV_DISABLE
# select.KQ_EV_ONESHOT
# select.KQ_EV_CLEAR
# select.KQ_EV_S
