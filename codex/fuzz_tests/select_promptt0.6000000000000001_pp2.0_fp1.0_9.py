import select
# Test select.select()

print('Entering blocking mode')
r, w, x = select.select([sys.stdin], [], [])
print('Leaving blocking mode')
print('r =', r)
print('w =', w)
print('x =', x)
