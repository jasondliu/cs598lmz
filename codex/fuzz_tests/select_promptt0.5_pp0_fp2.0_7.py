import select
# Test select.select()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',0))
s.listen(1)

(c,a) = s.accept()

print "Test 1"
r,w,e = select.select([c], [c], [c], 1)
print r,w,e

print "Test 2"
r,w,e = select.select([c], [], [], 1)
print r,w,e

print "Test 3"
r,w,e = select.select([], [c], [], 1)
print r,w,e

print "Test 4"
r,w,e = select.select([], [], [c], 1)
print r,w,e

print "Test 5"
r,w,e = select.select([], [], [], 1)
print r,w,e
