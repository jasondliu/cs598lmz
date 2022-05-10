import select
# Test select.select is accessible
x = select.select
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 6666))

class False(object):

    def fileno(self):
        return 3

print '*** default timeout'
print '  expecting [5, 6, 7]:', repr(select.select([5, 6, 7], [], []))
print '  expecting []:', repr(select.select([4], [], [], 0))

print '*** zero timeout'
print '  expecting [5, 6, 7]:', repr(select.select([5, 6, 7], [], [], 0))
print '  expecting []:', repr(select.select([4], [], [], 0))

print '*** within timeout'
delay = 6
x = select.select([s], [], [], delay)
print '  got', repr(x)
print '  expecting', delay, 'seconds delay'

print '*** just timeout'
delay = 10
before = time()
x = select.select([], [
