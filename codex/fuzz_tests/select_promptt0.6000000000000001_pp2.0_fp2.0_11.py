import select
# Test select.select() with a timeout:

r, w, x = select.select([], [], [], 0.5)
print(r, w, x)

r, w, x = select.select([], [], [], 0.0)
print(r, w, x)

r, w, x = select.select([], [], [], -1)
print(r, w, x)

r, w, x = select.select([], [], [], None)
print(r, w, x)

# Test select.select() with a file descriptor:

f = open('/dev/null', 'r')
try:
    r, w, x = select.select([f], [], [])
finally:
    f.close()

print(r, w, x)

# Test select.select() with a file descriptor and timeout:

f = open('/dev/null', 'r')
try:
    r, w, x = select.select([f], [], [], 0.5)
finally:
    f.close()

