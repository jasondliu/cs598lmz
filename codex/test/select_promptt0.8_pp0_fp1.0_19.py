import select
# Test select.select.

# Used to wait for events on "r" and "w".
r, w = os.pipe()

# wait for readability
rlist, wlist, xlist = select.select([r], [], [], 10)
print("rlist = {}, wlist = {}, xlist = {}".format(rlist, wlist, xlist))

# r should be readable
rlist, wlist, xlist = select.select([r], [], [], 0)
print("rlist = {}, wlist = {}, xlist = {}".format(rlist, wlist, xlist))

os.close(r)

# r will not be readable
rlist, wlist, xlist = select.select([r], [], [], 0)
print("rlist = {}, wlist = {}, xlist = {}".format(rlist, wlist, xlist))

# wait for writability
wlist, rlist, xlist = select.select([], [w], [], 10)
