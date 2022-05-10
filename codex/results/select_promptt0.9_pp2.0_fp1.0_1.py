import select
# Test select.select() not hang.

print "select() started"
timeout = 1
r, w, x = select.select([], [], [], timeout)
print "select() return after %fs" % timeout

print "end"
