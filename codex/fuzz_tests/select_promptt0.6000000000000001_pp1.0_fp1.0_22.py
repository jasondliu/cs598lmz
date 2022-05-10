import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# 返回一个三元素的元组，分别表示rlist, wlist, xlist中就绪的元素，如果超时则返回空元组
# rlist：可读的对象列表
# wlist：可写的对象列表
# xlist：发生异常的对象列表
# timeout：超时时间，单位秒，默认为永远等待
# 参数都可以是字符串、文件描述符、文件对象或其
