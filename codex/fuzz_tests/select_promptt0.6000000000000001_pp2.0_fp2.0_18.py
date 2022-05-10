import select
# Test select.select()
# select.select() -> (rlist, wlist, xlist)
# poll() -> poll object
# epoll() -> epoll object
# kqueue() -> kevent object

# select缺点：
# 1. 只能检测到fd收发数据，不能检测到fd的其他状态变化，比如连接关闭，超时等
# 2. 只能检测socket的fd，不能检测其他类型的fd
# 3. 在大量fd的情况下效率不高，因为它是顺序扫描的
# 4. 在win下不可用，只能在linux下使用
