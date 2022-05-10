import select
# Test select.select()

print 'Testing select.select()'

# Test select.select() with a timeout.
print 'Testing select.select() with a timeout.'
r, w, x = select.select([], [], [], 0.1)
print 'select.select() returned', r, w, x

# Test select.select() with a timeout of 0.
print 'Testing select.select() with a timeout of 0.'
r, w, x = select.select([], [], [], 0)
print 'select.select() returned', r, w, x

# Test select.select() with a timeout of -1.
print 'Testing select.select() with a timeout of -1.'
r, w, x = select.select([], [], [], -1)
print 'select.select() returned', r, w, x

print 'Done testing select.select()'
