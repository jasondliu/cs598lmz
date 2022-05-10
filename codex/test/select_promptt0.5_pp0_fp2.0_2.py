import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (not implemented on all platforms)
# timeout: if no object is ready, wait until a specified time out

# Return value: three lists of objects that are ready

# Monitor stdin and stdout

print('monitoring stdin and stdout')

while True:
    r, w, e = select.select([sys.stdin, ], [sys.stdout, ], [], 1)
    if r:
        print('ready for reading:', r)
        print(sys.stdin.readline())
    if w:
        print('ready for writing:', w)
