import select
# Test select.select
# select.select([inputs], [outputs], [inputs], timeout)
#  |- select reads will return when inputs is readable
#  |- select writes will return when outputs is writeable
#  |- select errors will retrun when any of inputs is exceptional
# Return value ``(readable, writable, errors)``.

import pyuv

def check(loop, handle, error):
    # input buffer
    i = os.pipe()
    # output buffer
    o = os.pipe()
    t = None
    # waiti max 100ms
    t = loop.timer(100, 0, lambda x:check.timeout(loop, x, i, o))
    # select
    r, w, e = select.select([i[0], o[1]], [o[0]], [], 1)
    # select timeout
    if not(r or w or e):
        check.timeout(loop, t, i, o)
