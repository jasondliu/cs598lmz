import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are all lists of file descriptors
# timeout is a float number in seconds
# select.select() returns three lists of file descriptors
# select.select() blocks until at least one of the file descriptors is ready for some kind of I/O
# select.select() raises an exception if the file descriptor is invalid

# select() 函数的第一个参数是一个列表，列表中的每一项是一个IO对象（文件对象）。
# 如果这个IO对象在这个列表中，那么这个函数会监测这个IO对象是否可读。
# 如果这个IO对
