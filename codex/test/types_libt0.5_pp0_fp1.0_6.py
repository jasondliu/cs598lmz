import types
types.FunctionType

# 元组
t = (1, 2, 3)
t = ('a', True, 123)
t[0]
t[-1]
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t

# 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
'Michael' in d
d.get('Thomas')
d.get('Thomas', -1)
d.pop('Bob')

# 集合
s = set([1, 1, 2, 2, 3, 3])
s
s.add(4)
s.add(4)
s.remove(4)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

# 字符串
'ABC'.encode('ascii')
