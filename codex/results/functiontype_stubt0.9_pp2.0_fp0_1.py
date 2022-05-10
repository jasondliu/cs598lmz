from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(dir(b))
print(dir(a))
print(a)
"""
b = {'a': 1}
c = 1

print(b[1])
"""
a = [i for i in range(10)]
b = [1, 2, 3, 4, 5]

print(a)
print(b)

"""
"""
a = {i: i*i for i in range(10)}
print(a)

b = {j: j+1 for j in a}
print(b)
# b.update({k: k+100})
# print(b)
b.setdefault(10, 100)
print(b)
tb = [(i, i*2) for i in range(10)]
print(tb)

print(list(zip('abcd', '1234')))
print(dict(zip('abcd', '1234')))

"""
print(b.values())
print(b.keys())
print(
