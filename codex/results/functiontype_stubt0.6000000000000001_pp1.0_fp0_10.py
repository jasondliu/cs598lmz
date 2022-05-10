from types import FunctionType
a = (x for x in [1])
print type(a)
print type(sum)
print isinstance(a, Iterator)
print isinstance(sum, FunctionType)

# 字典 保存键值对
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
print d.get('Bob', 'none')

# set 保存不重复的元素
s = set([1, 2, 3])
print s
s.add(4)
s.remove(4)
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print s1 & s2
print s1 | s2

# str 可以当作list 使用
print 'ABC'.encode('ascii')
print '中文'.encode('utf-8')
print len('中文')
print len('中文'.encode('utf-8'))

# 函数
def my_
