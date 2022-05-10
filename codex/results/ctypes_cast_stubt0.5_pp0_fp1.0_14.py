import ctypes
ctypes.cast(a, ctypes.py_object).value

a = np.arange(12)
b = a
b is a

b.shape = 3,4
a.shape

def f(x):
    print(id(x))

id(a)
f(a)

c = a.view()
c is a

c.base is a

c.flags.owndata

c.shape = 2,6
a.shape

c[0,4] = 1234
a

s = a[:,1:3]
s[:] = 10
a

d = a.copy()
d is a

d.base is a

d[0,0] = 9999
a

# 创建数组
# 可以通过一个列表来创建数组
a = np.array([2,3,4])
a

a.dtype

b = np.array([1.2, 3.5, 5
