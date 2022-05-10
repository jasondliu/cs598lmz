import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test select.epoll()
epfd = select.epoll()
epfd.close()

# Test select.kqueue()
kqfd = select.kqueue()
kqfd.close()

# Test select.poll()
pfd = select.poll()
pfd.close()

# Test select.select()
rfd, wfd, xfd = select.select([], [], [])

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(-1)
signal.set_wakeup_fd(1)

# Test select.devpoll()
dpd = select.devpoll()
dpd.close()

# Test select.epoll()
epfd = select.epoll()
epfd.close()

# Test _multiprocessing.rec
