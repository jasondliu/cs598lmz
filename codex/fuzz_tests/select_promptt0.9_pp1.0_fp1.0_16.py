import select
# Test select.select
num_fds = 100
print 'Testing select on %d file descriptors...' % num_fds
inputs = []
for i in xrange(num_fds):
    r, w, e = select.select([], [], range(num_fds), 1.0)
    if len(r):
        print 'Unexpected inputs on %r' % r
    if len(e) == num_fds:
        print 'Expected error objects'
    else:
        print 'Did not get enough error objects (%d)' % len(e)
    inputs.append(r)
# Test os.poll
print 'Testing select on %d file descriptors...' % num_fds
inputs = []
p = select.poll()
for i in xrange(num_fds):
    p.poll(1.0)
    if len(r):
        print 'Unexpected inputs on %r' % r
    if len(e) == num_fds:
        print 'Expected error objects'
    else:
        print 'Did not get enough error objects (%
