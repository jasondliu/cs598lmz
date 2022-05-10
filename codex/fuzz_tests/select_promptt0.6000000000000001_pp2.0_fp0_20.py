import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: 待读文件对象;
# wlist: 待写文件对象;
# xlist: 待异常文件对象;
# timeout: 超时时间, 单位: 秒.
# select.select()返回值:
# 如果超时返回空列表,
# 否则返回一个元组, 包含三个列表,
# 分别是可读, 可写, 异常文件对象列表.
# 例:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])

# 客户
