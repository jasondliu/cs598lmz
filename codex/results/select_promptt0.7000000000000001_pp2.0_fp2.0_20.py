import select
# Test select.select() 
# select.select(rlist, wlist, xlist[, timeout])

# rlist：待读文件的列表；
# wlist：待写文件的列表；
# xlist：待错误文件的列表；
# timeout：超时时间，单位为秒。
# select监听的三个列表中，只要有一个元素发生了变化，就返回这三个列表，
# 不阻塞，立刻返回，只要有一个文件发生变化，就返回，返回的是文件发生变
