import select
# Test select.select with a bad timeout
try:
    select.select([], [], [], 0.5)
except ValueError:
    pass
try:
    select.select([], [], [], -1)
except ValueError:
    pass

# Test the select.poll class
p = select.poll()
if verbose:
    print 'poll support:',
    if hasattr(p, 'modify'):
        print 'modify'
    if hasattr(p, 'poll'):
        print 'poll'
    if hasattr(p, 'register'):
        print 'register'
    if hasattr(p, 'unregister'):
        print 'unregister'
    print

# Create a couple of sockets
s1, s2 = socket.socketpair()
socket_map = {
    s1.fileno(): s1,
    s2.fileno(): s2,
}

for i in range(len(args)):
    if verbose:
        print 'args[%d] is %s' % (i, args[i])

for
