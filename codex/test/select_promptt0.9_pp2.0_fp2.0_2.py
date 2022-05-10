import select
# Test select.select
# 问题：IO多路复用的优势是什么？

# select: 负责监控IO
"""
r_list: IO等待读取
w_list: IO等待写入
x_list: 异常
最后一个为timeout
"""
import socket

s = socket.socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 管理socket便于管理
inputs = [s]
# 用于返回
outputs = []

# 监控socket
# 问题是什么？为什么要监控socket？
# 未监控的情况下，是否要创
