import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
print('Selecting...')
rlist, wlist, xlist = select.select([sys.stdin], [], [])
print('Ready:', rlist)
line = sys.stdin.readline()
print('You said:', line)
