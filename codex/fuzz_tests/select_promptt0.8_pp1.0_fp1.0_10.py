import select
# Test select.select()


timeout = 2
rlist, wlist, xlist = select.select([sys.stdin], [], [], timeout)
if rlist:
    s = sys.stdin.readline()
    print 'Do something with %s' % s
else:
    print 'Timed out'
