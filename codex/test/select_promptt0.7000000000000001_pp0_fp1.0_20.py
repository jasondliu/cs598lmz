import select
# Test select.select()

print("Testing select.select()")
rlist, wlist, xlist = select.select([], [], [], 0)
print("wait 0 second, rlist: {}, wlist: {}, xlist: {}".format(rlist, wlist, xlist))

rlist, wlist, xlist = select.select([], [], [], 3)
print("wait 3 seconds, rlist: {}, wlist: {}, xlist: {}".format(rlist, wlist, xlist))

rlist, wlist, xlist = select.select([sys.stdin], [], [], 3)
print("wait 3 seconds, rlist: {}, wlist: {}, xlist: {}".format(rlist, wlist, xlist))

rlist, wlist, xlist = select.select([sys.stdin], [], [], 0)
