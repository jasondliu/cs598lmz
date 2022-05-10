import select
# Test select.select()
print('Selecting')
r, w, e = select.select([], [], [], 0.1)
print('r =', r)
print('w =', w)
print('e =', e)
