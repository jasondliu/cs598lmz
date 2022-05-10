import select
# Test select.select
print 'select.select([], [], [], 0.0)', select.select([], [], [], 0.0)

# Test select.poll
poll_obj = select.poll()
print 'poll_obj.register(0, select.POLLIN)', poll_obj.register(0, select.POLLIN)
print 'poll_obj.poll(0.0)', poll_obj.poll(0.0)
print 'poll_obj.unregister(0)', poll_obj.unregister(0)
print 'poll_obj.poll(0.0)', poll_obj.poll(0.0)

# Test select.epoll
epoll_obj = select.epoll()
print 'epoll_obj.register(0, select.EPOLLIN)', epoll_obj.register(0, select.EPOLLIN)
print 'epoll_obj.poll(0.0)', epoll_obj.poll(0.0)
print 'epoll_obj.unregister(0)', epoll_obj.unregister(0)
print
