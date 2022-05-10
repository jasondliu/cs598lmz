import select
# Test select.select()
# 注意，select 所关心的是 socket 对象，而不是文件对象
# select.select(rlist, wlist, xlist[, timeout])
# rlist: 待读文件列表
# wlist: 待写文件列表
# xlist: 待错误处理文件列表
# timeout: 超时时间，单位为秒，如果为None，永远阻塞

# 返回三个列表，分别是可读、可写、错误的文件列表，其中错误文件列表一般为空

