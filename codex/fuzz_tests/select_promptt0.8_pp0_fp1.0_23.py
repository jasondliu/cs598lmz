import select
# Test select.select
r, w, e = select.select( [sys.stdin], [], [], 2)
print r
