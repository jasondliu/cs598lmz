import select
# Test select.select()
print "Calling select.select()"
rlist, wlist, xlist = select.select([sys.stdin], [], [], 0.0)
print "Returned from select.select()"
if rlist:
    print "Data is available at stdin"
else:
    print "Timed out. No data is available at stdin"

# Test select.poll()
print "Calling select.poll()"
p = select.poll()
p.register(sys.stdin.fileno(), select.POLLIN)
events = p.poll(0.0)
print "Returned from select.poll()"
if events:
    print "Data is available at stdin"
else:
    print "Timed out. No data is available at stdin"

# Test select.epoll()
print "Calling select.epoll()"
e = select.epoll()
e.register(sys.stdin.fileno(), select.EPOLLIN)
events = e.poll(0.0)
print "Returned from select.epoll()"
if events
