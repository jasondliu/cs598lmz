import select
# Test select.select()

# Linux, Windows, MacOS X
# select.select(rlist, wlist, xlist[, timeout])
# rlist -- 待读文件列表；
# wlist -- 待写文件列表；
# xlist -- 异常文件列表；
# timeout -- 操作超时时间，None表示阻塞。

inputs = [input('请输入：') for i in range(3)]
rs, ws, xs = select.select(inputs, [], [], 3)

print(rs)
print(ws)
print(xs)
