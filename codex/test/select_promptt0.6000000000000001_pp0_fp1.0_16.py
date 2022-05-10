import select
# Test select.select()
r, w, x = select.select([sys.stdin], [], [])
print(r)
print(w)
print(x)
