import select
# Test select.select
rlist, wlist, xlist = select.select([sys.stdin], [], [], 5)
if rlist:
    print rlist
else:
    print 'Timeout'
# Test select.poll

p = select.poll()
p.register(sys.stdin, select.POLLIN)
f = p.poll(5000)

if f:
    print f
else:
    print 'Timeout'
print 'Done'
