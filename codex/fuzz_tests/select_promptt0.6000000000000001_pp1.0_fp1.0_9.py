import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist 三个参数都是文件描述符的列表，比如[sys.stdin]
# timeout 是一个可选的参数，单位是秒，如果在指定时间内没有输入就会报错，如果是0就不会等待，如果是None就会一直等待
# rlist, wlist, xlist 分别表示可读，可写，异常文件描述符
# 返回值是 rlist, wlist, xlist 三个
