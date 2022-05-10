import select
# Test select.select
# select(rlist, wlist, xlist[, timeout])
# rlist：等待监听的文件描述符列表，如果为空表，则select会一直等待，直到有文件描述符就绪
# wlist：等待写入的文件描述符列表
# xlist：等待异常的文件描述符列表
# timeout：超时时间，单位是秒

# 返回值：
# rlist：可读的文件描述符列表
# wlist：可写的文件描述
