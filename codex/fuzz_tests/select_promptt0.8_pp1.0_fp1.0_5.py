import select
# Test select.select(rlist, wlist, xlist)

# 1) simple test
# returns 3 empty lists when timeout=0

print select.select([], [], [], 0)

# 2) test with file handles
# returns non-empty lists if there are filehandles in rlist, wlist, xlist
# (depending on the type of filehandles or if they are open)

print select.select([sys.stdin], [sys.stdout], [sys.stderr], 0)
