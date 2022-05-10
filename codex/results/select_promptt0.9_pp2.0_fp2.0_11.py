import select
# Test select.select with large timeout to ensure it is not
# subject to the signed 32-bit integer overflow that the
# Windows select() function can suffer from.
timeout = 315360000.0
rlist, wlist, xlist = select.select([], [], [], timeout)
# The magic number is the result of select.select with a
# large timeout parameter.
if rlist is not None or wlist is not None or xlist is not None:
    raise ValueError("select.select returned wrong values:", rlist, wlist, xlist)
