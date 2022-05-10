import select
# Test select.select
__author__ = 'Yuanyuan Zhang'
__date__ = '2015-3-25'
__modified__ = '2015-3-25'
import select
import time

TIMEOUT = 2

# 2 sockets
rlist, wlist, elist = select.select([], [], [], TIMEOUT)

if not (rlist or wlist or elist):
    print "Time out. Closing."
    rlist.close()
    wlist.close()

time_left = TIMEOUT
while rlist or wlist or elist:
    rl, wl, el = select.select([], [], [], time_left)

    if rl:
        print "rlist: ", rl
    if wl:
        print "wlist: ", wl
    time_left = time_left - (time.time() - start)
    if time_left <= 0:
        print "Closing after TIMEOUT"
        rlist.close()
        wlist.close()
        break
