import select
# Test select.select
print >>sys.stderr, 'Testing select.select...'

# we need at least 2 pipe fds to test
fd1, fd2 = os.pipe()
fd3, fd4 = os.pipe()
fd2, fd3 = os.dup(fd2), os.dup(fd3)

# see if select works with no fds ready
r, w, e = select.select([fd1], [fd2], [], 1)
if r or w or e:
    print >>sys.stderr, 'no fds ready:', r, w, e

# but if we pass in empty lists, we should get back empty lists
