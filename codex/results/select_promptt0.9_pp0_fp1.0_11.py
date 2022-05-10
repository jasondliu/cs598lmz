import select
# Test select.select() with multiple invalid file descriptors
for r in (()), (3, 4):
    k = select.select(r, r, r)
    if k != ([], [], []):
        print 'error', k
    k = select.select(r, r, r, 0.1)
    if k != ([], [], []):
        print 'error', k
import select

# Test epoll
ep = select.epoll()

# Test eventmask argument
ep.register(1,0)
ep.modify(1, select.EPOLLIN|select.EPOLLPRI|select.EPOLLOUT|\
          select.EPOLLERR|select.EPOLLHUP|select.EPOLLET)

# Test control of edge triggering
ep.modify(1, select.EPOLLERR|select.EPOLLET)
ep.modify(1, select.EPOLLERR)

# Test control of one-shot mode
ep.modify(1, select.EPOLLERR|select.EPOLLONESHOT
