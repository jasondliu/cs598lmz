import select
# Test select.select

rlist = [0, 1, 2]
wlist = [0, 1, 2]
xlist = [0, 1, 2]

print(select.select(rlist, wlist, xlist, 2))
