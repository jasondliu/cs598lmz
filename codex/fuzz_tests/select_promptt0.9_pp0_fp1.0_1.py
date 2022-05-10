import select
# Test select.select()
something_readable, something_writable, something_exp = select.select(inputs, outputs, inputs, timeout=0)

# Test select.poll()
poll_obj = select.poll()
poll_obj.register(socket)
events = poll_obj.poll(timeout)

# Test select.epoll()
epoll_obj = select.epoll()
epoll_obj.register(socket)
events = epoll_obj.epoll(timeout)

# Test select.kepoll() on UNIX
kepoll_obj = select.kepoll()
kepoll_obj.close()
kepoll_obj.register(socket)
kepoll_obj.add(socket)
kepoll_obj.remove(socket)
kepoll_obj.modify(socket)
kepoll_obj.update({socket: select.KEPOLL_ADD})
events = kepoll_obj.poll(timeout)

# Test select.kepoll() on UNIX-like platforms (Linux, Cygwin, OS X, *BSD)
kepoll_obj = select.kepoll()
kepoll_
