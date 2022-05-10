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

