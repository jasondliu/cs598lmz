import select
# Test select.select

print 'select.select(rlist, wlist, xlist, timeout=0.0):'
print '  rlist: ', select.select([1, 2, 3], [], [], 0.0)
print '  wlist: ', select.select([], [1, 2, 3], [], 0.0)
print '  xlist: ', select.select([], [], [1, 2, 3], 0.0)
print '  timeout: ', select.select([], [], [], 0.1)
print

print 'select.select(rlist, wlist, xlist):'
print '  rlist: ', select.select([1, 2, 3], [], [])
print '  wlist: ', select.select([], [1, 2, 3], [])
print '  xlist: ', select.select([], [], [1, 2, 3])
print '  timeout: ', select.select([], [], [])
print

print 'select.select(rlist, wlist, xlist, timeout=None):'
print '  rlist:
