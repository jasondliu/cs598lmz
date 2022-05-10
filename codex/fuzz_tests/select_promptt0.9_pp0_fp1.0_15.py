import select
# Test select.select
retVal = select.select([sys.stdin], [], [], 5.0)
if not retVal[0] or eq(retVal[0], []) or eq(retVal[0], []):
    raise TestFailed, 'Unexpected return value from select.select: %s'%retVal

# Test select.poll
p = select.poll()
p.register(sys.stdin.fileno(), select.POLLIN)
retVal = p.poll(5.0)
if not retVal or eq(retVal, []) or eq(retVal, []):
    raise TestFailed, 'Unexpected return value from select.poll: %s'%retVal

# Verify that module attributes really exist
import sys
getattr(sys, 'stdin')
getattr(sys, 'stdout')
getattr(sys, 'stderr')

# Test 'while 1: pass'
while 1:
    pass

# Test 'while 1: pass'
x = 1
while x:
    x = x-1
    pass

# Test 'pass
