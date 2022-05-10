import select
# Test select.select() function

def testcase_fn(s, wlist, xlist, timeout):
    print "Before select: wlist = %r, xlist = %r, timeout = %r" % (wlist, xlist, timeout)
    rlist, wlist, xlist = select.select(s, wlist, xlist, timeout)
    print "After select: rlist = %r, wlist = %r, xlist = %r" % (rlist, wlist, xlist)
    
s = []
s.append(sys.stdin)
wlist = []
xlist = []
timeout = 1.0

print "When s is empty, everything should return empty lists or None"
testcase_fn(s, wlist, xlist, timeout)

print "\nWhen s is not empty, but wlist, xlist and timeout are empty, get rlist"
s.append(sys.stderr)
testcase_fn(s, wlist, xlist, timeout)

print "\nWhen wlist is not empty and timeout > 0, get wlist"


