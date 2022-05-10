import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist: 待检测的IO对象列表
# timeout: 设置超时时间，为None时不设置超时，为0时立即返回
# select.select()返回的三个列表中的元素都是IO对象
# 可写的列表中的IO对象，可以使用send()方法向其中写入数据
# 可读的列表中的IO对象，可以使用recv()方法从其中读取数据
# 异常的列表中的IO对象
