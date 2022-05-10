import socket
socket.if_indextoname(4)
import os

if not os.path.exists('/tmp/eth_idxtoi.txt'):
    eth_idxtoi = dict()
    for idx in range(0,1024):
        try:
            ifinfo = psutil.net_if_stats()
            eth_idxtoi[idx] = ifinfo[idx].name
        except:
            pass
    with open('/tmp/eth_idxtoi.txt','w') as f:
        print >> f,  repr(eth_idxtoi)
