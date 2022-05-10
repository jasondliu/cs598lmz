import select
# Test select.select()
import sys
print "initially: ", select.poll()

print >>sys.stderr, '\nopen 2 files:'
print >>sys.stderr, '\nTest polling'
sys.stderr.flush()

f1 = open('readme')
print "get fd = %d" % f1.fileno()
print "polling: ", select.poll()

f2 = open('sys.py')
print "get fd = %d" % f2.fileno()
print "polling: ", select.poll()

print >>sys.stderr, '\nnote that the select module is not the same as p-module'
sys.stderr.flush()

print >>sys.stderr, '\npoll already open files'
print >>sys.stderr, '\tvote for f1 and f2 to be writable'
sys.stderr.flush()

p = select.poll()
p.register(f1, select.POLLOUT)
p.register(f2, select.POLLOUT
