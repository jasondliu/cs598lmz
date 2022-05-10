import select
# Test select.select
# select.select(rlist, wlist, xlist)
# 返回一个 tuple，(rl, wl, xl)，分别为三个 list 中可读可写的 rlist,
# wlist, xlist
# rlist 中的套接字可读 ==> rl
# wlist 中的套接字可写 ==> wl
# xlist 中的套接字可读可写 ==> xl

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定到端口
serversocket.bind(('localhost', 8089))
# 最大连接数
serversocket.listen(5)
# 所有套接字都放在一个列表里面
servers
