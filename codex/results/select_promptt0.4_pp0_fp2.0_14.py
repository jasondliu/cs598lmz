import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist: 一个可读, 可写, 可异常的文件描述符列表, 如果为空, 则超时
# timeout: 超时时间, 单位为秒, 如果为0, 则立即返回
# 返回值: 三元组 (rlist, wlist, xlist)
# rlist: 可读文件描述符列表
# wlist: 可写文件描述符列表
# xlist: 可异常的文件描述符列表

import socket
import select

s = socket.socket(socket.
