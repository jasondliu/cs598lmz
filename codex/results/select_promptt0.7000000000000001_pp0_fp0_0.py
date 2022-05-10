import select
# Test select.select
# select.select([], [], [])

# Test select.poll
poll = select.poll()
# poll.poll()

# Test select.epoll
epoll = select.epoll()
# epoll.poll()

# Test select.devpoll
devpoll = select.devpoll()
# devpoll.poll()

# Test select.kqueue
kqueue = select.kqueue()
# kqueue.control([], 0, 0)
# kqueue.control([], 0, 0, None)

# Test select.kevent
# select.kevent([], [], [])

# Test signal.signal
signal.signal(signal.SIGIO, signal.SIG_DFL)

# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(0)

# Test signal.getsignal
signal.getsignal(signal.SIGIO)

#
