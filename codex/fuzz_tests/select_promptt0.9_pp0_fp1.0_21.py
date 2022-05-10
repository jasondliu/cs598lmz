import select
# Test select.select()

print """a timeout of 1 second is used in the select function"""

# no timeout
print "  select([], [], [], None)"
r, w, e = select.select([], [], [], None)
print "    ", r, w, e
print "  passed -- nothing to do, so nothing waiting"

print "  select([], [], [], 0)"
r, w, e = select.select([], [], [], 0)
print "    ", r, w, e
print "  passed -- nothing to do, so we go straight to completion"

# timeout
print "  select([], [], [], 1)"
r, w, e = select.select([], [], [], 1)
print "    ", r, w, e
print "  passed -- nothing to do, so we wait until we timeout"

# we have something waiting...
class X:
    def fileno(self): return 1

print "  select([X()], [], [], 0)"
r, w, e = select.select([X()], [], [], 0
