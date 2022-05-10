import select
# Test select.select()
fs = [open(x) for x in ['a', 'b', 'c']]

print('first time')
r, w, x = select.select(fs, [], [])
print(r)

print('second time')
r, w, x = select.select(fs, [], [])
print(r)

print('third time')
r, w, x = select.select(fs, [], [])
print(r)

print('close')
for f in fs:
    f.close()

print('last time')
r, w, x = select.select(fs, [], [])
print(r)
