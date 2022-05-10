import select
# Test select.select()

# select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist: 可读，可写，异常列表
# timeout: 最长等待时间
# 返回值：(rlist, wlist, xlist)

# 创建两个socket
s1 = socket.socket()
s2 = socket.socket()

# 绑定端口
s1.bind(('127.0.0.1', 8001))
s2.bind(('127.0.0.1', 8002))

# 监听
s1.listen(5)
s2.listen(5)

# 创建epoll对象
ep = select.epoll()
