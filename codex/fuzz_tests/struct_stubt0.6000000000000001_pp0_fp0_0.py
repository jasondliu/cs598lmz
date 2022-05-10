from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

print('{0.name} at {0.filename}:{0.lineno}'.format(getframeinfo(currentframe())))

# 字符串连接操作
names = ['raymond', 'rachel', 'matthew']
print(', '.join(names))

# 多值赋值
x, y, z = 1, 2, 3
print(x, y, z)

# 在字典中将键映射到多个值上
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

# 在字典中将键映射到多个值上
d = defaultdict(set)
d['a'
