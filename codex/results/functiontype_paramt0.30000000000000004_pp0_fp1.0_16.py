from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 元组
t = (1, 2, 3, 4)
t = 1, 2, 3, 4
t = tuple([1, 2, 3, 4])
t = tuple('spam')
t[i]
t[i][j]
t.index(4)
t.count(4)

# 列表
l = [1, 2, 3, 4]
l = list('spam')
l[i] = 42
l[i:j] = [4, 5, 6]
l.append(4)
l.extend([5, 6, 7])
l.insert(i, x)
l.remove(x)
l.pop(i)
l.index(x)
l.count(x)
l.sort()
l.reverse()

# 字典
d = {'name': 'Bob', 'age': 40}
d = dict(name='Bob', age=40)
d = dict(zip(['name', 'age'
