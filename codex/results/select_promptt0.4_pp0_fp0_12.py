import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist 分别是可读，可写，异常的文件描述符列表
# timeout 是超时时间
# 返回值是三个列表，分别是可读，可写，异常的文件描述符列表
# 如果超时，三个列表都是空

# select.select() 可以使用在非阻塞的IO上，也可以使用在阻塞的IO上
# 在阻塞的IO上使用select.select()，可以让
